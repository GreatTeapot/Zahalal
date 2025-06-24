from django.db import models

class FeaturedCard(models.Model):
    card = models.ForeignKey(
        to='cards.Card',
        on_delete=models.CASCADE,
        related_name='featured_entries',
        verbose_name='Карточка'
    )

    class Meta:
        verbose_name = 'Рекламная карточка'
        verbose_name_plural = 'Рекламные карточки'

    def __str__(self):
        return f"Featured: {self.card.description[:20]}"