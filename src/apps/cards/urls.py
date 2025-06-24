from django.urls import path
from apps.cards.views.card import CardDetailView, CardSearcherListAPIView, FeaturedCardListAPIView, CardListAPIView, TypesByCategoryAPIView, CardsByTypeAPIView


urlpatterns = [
    path('details/<int:pk>/', CardDetailView.as_view(), name='card-full-info'),
    path('searcher', CardSearcherListAPIView.as_view(), name='card-search'),
    path('', CardListAPIView.as_view(), name='card-list'),
    path('featured', FeaturedCardListAPIView.as_view(), name='featured-card-list'),
    path('types', TypesByCategoryAPIView.as_view(), name='types-by-category'),
    path('types/cards/', CardsByTypeAPIView.as_view(), name='cards-by-types'),
]