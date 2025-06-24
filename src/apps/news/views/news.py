from rest_framework.generics import ListAPIView, RetrieveAPIView
from apps.news.serializers.news import NewsPostShortSerializer, NewsPostFullSerializer
from apps.news.services.news_service import get_all_news_posts, get_news_post_by_id
from apps.news.models.news import NewsPost


class NewsPostListAPIView(ListAPIView):
    serializer_class = NewsPostShortSerializer

    def get_queryset(self):
        return get_all_news_posts()


class NewsPostDetailAPIView(RetrieveAPIView):
    serializer_class = NewsPostFullSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return NewsPost.objects.prefetch_related('photos', 'videos')