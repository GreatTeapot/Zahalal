from rest_framework import serializers
from apps.reviews.models.review import Review

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['author', 'review', 'stars', 'card']

    def create(self, validated_data):
        return Review.objects.create(**validated_data, is_approved=False)
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'author', 'review', 'stars']