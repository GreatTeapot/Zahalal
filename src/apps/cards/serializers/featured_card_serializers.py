from rest_framework import serializers
from apps.cards.serializers.card_serializers import CardListSerializer
from apps.cards.models.featured_card import FeaturedCard

class FeaturedCardListSerializer(serializers.ModelSerializer):
    card = CardListSerializer()

    class Meta:
        model = FeaturedCard
        fields = ['id', 'card']