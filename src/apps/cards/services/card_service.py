from apps.cards.models.card import Card
from django.db.models import Avg, Q

def get_cards_by_type(card_type):
    return Card.objects.filter(type=card_type).annotate(
        avg_rating=Avg('reviews__stars', filter=Q(reviews__is_approved=True))
    )

def get_all_cards():
    return Card.objects.all()

def get_all_cards():
    return Card.objects.select_related('type').all()