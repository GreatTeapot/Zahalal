from rest_framework import serializers
from apps.cards.models.card import Card, CardPhoto, CardVideo, CardWorkDay
from apps.reviews.serializers.review import ReviewSerializer
from common.pagination import CustomPagination
from apps.reviews.services.review_service import get_average_rating_for_card


class CardPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardPhoto
        fields = ['id', 'image']


class CardVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardVideo
        fields = ['id', 'video']


class CardWorkDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = CardWorkDay
        fields = ['id', 'dayoftheweek', 'starts_work', 'stops_work']


class CardFullInfoSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    type = serializers.StringRelatedField()
    location = serializers.SerializerMethodField()
    photos = CardPhotoSerializer(many=True, read_only=True)
    videos = CardVideoSerializer(many=True, read_only=True)
    work_days = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    face_img = serializers.ImageField()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Card
        fields = [
            'id', 'title', 'face_img', 'category', 'type', 'description',
            'phone_number', 'whatsapp', 'telegram', 'site',
            'work_days', 'location', 'address', 'city', 'average_rating',
            'photos', 'videos', 'reviews'
        ]

    def get_average_rating(self, obj):
        return get_average_rating_for_card(obj)

    def get_location(self, obj):
        if obj.location:
            return {
                'name': obj.location.name,
                'latitude': obj.location.latitude,
                'longitude': obj.location.longitude
            }
        return None

    def get_work_days(self, obj):
        work_days_qs = obj.cardworkday_set.all()
        return CardWorkDaySerializer(work_days_qs, many=True).data

    def get_reviews(self, obj):
        request = self.context.get('request')
        reviews_qs = obj.reviews.filter(is_approved=True).order_by('-created_at')

        paginator = CustomPagination()
        paginator.page_size = 5
        paginated_reviews = paginator.paginate_queryset(reviews_qs, request)

        serializer = ReviewSerializer(paginated_reviews, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data).data