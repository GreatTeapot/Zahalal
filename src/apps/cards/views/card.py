from rest_framework.generics import RetrieveAPIView, ListAPIView
from apps.cards.models.card import Card
from apps.cards.models.featured_card import FeaturedCard
from apps.cards.models.type import Type
from apps.cards.serializers.card_full_info_serializers import CardFullInfoSerializer
from apps.cards.serializers.card_serializers import CardListSerializer
from apps.cards.serializers.featured_card_serializers import FeaturedCardListSerializer
from apps.cards.serializers.type_serializers import TypeSerializer
from common.pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from django.db.models import Q
from rest_framework.exceptions import ValidationError
from django.core.cache import cache
import hashlib
import json


def get_cache_key(request, prefix: str):
    params = json.dumps(request.query_params, sort_keys=True)
    key_raw = f"{prefix}:{params}"
    return hashlib.md5(key_raw.encode()).hexdigest()


class CardDetailView(RetrieveAPIView):
    queryset = Card.objects.all().prefetch_related('photos', 'videos', 'reviews')
    serializer_class = CardFullInfoSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(name='page', description='Номер страницы отзывов', required=False, type=int, location=OpenApiParameter.QUERY),
            OpenApiParameter(name='page_size', description='Количество отзывов на странице', required=False, type=int, location=OpenApiParameter.QUERY),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class FeaturedCardListAPIView(ListAPIView):
    serializer_class = FeaturedCardListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['card__category']
    pagination_class = CustomPagination

    def get_queryset(self):
        key = get_cache_key(self.request, "featured_cards")
        data = cache.get(key)
        if data:
            return data
        qs = FeaturedCard.objects.select_related('card__category')
        cache.set(key, qs, 300)
        return qs


class CardSearcherListAPIView(ListAPIView):
    serializer_class = CardListSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(name='search', description='Поиск по названию, типу, адресу, городу', required=False, type=str, location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample("Поиск по городу Бишкек", value="Бишкек", summary="search=Бишкек"),
                    OpenApiExample("Поиск по адресу Navat", value="Navat", summary="search=Navat"),
                ]),
            OpenApiParameter(name='city', description='Фильтр по городу', required=False, type=str, location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample("Фильтр по городу Бишкек", value="Бишкек", summary="city=Бишкек")
                ]),
        ],
        description="Примеры запросов:\n- /api/cards/?search=Бишкек\n- /api/cards/?city=Бишкек&search=чайхана"
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        key = get_cache_key(self.request, "card_search")
        data = cache.get(key)
        if data:
            return data

        queryset = Card.objects.all()
        search = self.request.query_params.get('search')
        city = self.request.query_params.get('city')

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(type__type__icontains=search) |
                Q(address__icontains=search) |
                Q(city__icontains=search)
            )
        if city:
            queryset = queryset.filter(city__icontains=city)

        cache.set(key, queryset, 300)
        return queryset


class CardListAPIView(ListAPIView):
    serializer_class = CardListSerializer
    pagination_class = CustomPagination

    @extend_schema(
        parameters=[
            OpenApiParameter(name='cat_id', description='Фильтр по ID категории', required=False, type=int, location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample("Фильтр по категории с ID 1", value=1, summary="cat_id=1"),
                    OpenApiExample("Фильтр по категории с ID 3", value=3, summary="cat_id=3"),
                ])
        ],
        description="Примеры: /api/cards/?cat_id=1"
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        key = get_cache_key(self.request, "card_list")
        data = cache.get(key)
        if data:
            return data

        queryset = Card.objects.all()
        cat_id = self.request.query_params.get('cat_id')
        if cat_id:
            queryset = queryset.filter(category__id=cat_id)

        cache.set(key, queryset, 300)
        return queryset


class TypesByCategoryAPIView(ListAPIView):
    serializer_class = TypeSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(name='cat_id', description='ID категории (например: Еда)', required=True, type=int, location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample("Еда", value=1, summary="cat_id=1"),
                    OpenApiExample("Спорт", value=2, summary="cat_id=2"),
                ])
        ],
        description="Типы карточек по категории",
        responses=TypeSerializer(many=True)
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        cat_id = self.request.query_params.get("cat_id")
        if not cat_id:
            raise ValidationError({"cat_id": "Этот параметр обязателен."})

        key = f"types_by_category:{cat_id}"
        data = cache.get(key)
        if data:
            return data

        queryset = Type.objects.filter(cards__category__id=cat_id).distinct()
        cache.set(key, queryset, 300)
        return queryset


class CardsByTypeAPIView(ListAPIView):
    serializer_class = CardListSerializer
    pagination_class = CustomPagination

    @extend_schema(
        parameters=[
            OpenApiParameter(name='cat_id', description='ID категории', required=True, type=int, location=OpenApiParameter.QUERY),
            OpenApiParameter(name='type_id', description='ID типа', required=True, type=int, location=OpenApiParameter.QUERY),
        ],
        description="Карточки по категории и типу",
        responses=CardListSerializer(many=True),
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        cat_id = self.request.query_params.get("cat_id")
        type_id = self.request.query_params.get("type_id")

        if not cat_id or not type_id:
            raise ValidationError("Параметры cat_id и type_id обязательны.")

        key = f"cards_by_type:{cat_id}:{type_id}"
        data = cache.get(key)
        if data:
            return data

        queryset = Card.objects.filter(category__id=cat_id, type__id=type_id)
        cache.set(key, queryset, 300)
        return queryset