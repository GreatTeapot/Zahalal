from apps.cards.models.featured_card import FeaturedCard

def get_all_featured_cards():
    return FeaturedCard.objects.select_related('card', 'card__category').all()