from rest_framework import generics
from apps.categories.models import Category
from apps.categories.serializers.category import CategorySerializer

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer