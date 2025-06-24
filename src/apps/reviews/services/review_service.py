from apps.reviews.models.review import Review
from django.db.models import Avg

def get_average_rating_for_card(card):
    reviews = Review.objects.filter(card=card, is_approved=True)
    if reviews.exists():
        return round(reviews.aggregate(Avg('stars'))['stars__avg'], 1)
    return None  