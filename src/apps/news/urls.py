from django.urls import path
from apps.news.views.news import NewsPostListAPIView, NewsPostDetailAPIView

urlpatterns = [
    path('', NewsPostListAPIView.as_view(), name='news-list'),
    path('<int:id>/', NewsPostDetailAPIView.as_view(), name='news-detail'),
]