from apps.cards.models.type import Type
from rest_framework import serializers

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'