from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from apps.reviews.serializers.review import ReviewCreateSerializer

class ReviewCreateView(CreateAPIView):
    serializer_class = ReviewCreateSerializer
    permission_classes = [AllowAny]