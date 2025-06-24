from rest_framework import serializers
from apps.cards.models.card import Card
from apps.reviews.services.review_service import get_average_rating_for_card

class CardListSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Card
        fields = ['id', 'title', 'type', 'address', 'average_rating', 'face_img']

    def get_type(self, obj):
        return obj.type.type if obj.type else None

    def get_average_rating(self, obj):
        return get_average_rating_for_card(obj)
    