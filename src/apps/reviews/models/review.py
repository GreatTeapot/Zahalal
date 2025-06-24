from django.db import models
from common.models.base import BaseModel
from django.conf import settings

class Review(BaseModel):
    """
    Модель Отзыва.

    Аттрибуты:
    - author: пользователь, оставивший отзыв
    - stars: оценка
    - review: текст отзыва
    - is_approved: одобрен ли отзыв
    """

    card = models.ForeignKey("cards.Card", related_name='reviews', on_delete=models.CASCADE)

    author = models.CharField(
        max_length=255
    )

    STARS_CHOICES = [(i, str(i)) for i in range(1, 6)] 

    stars = models.PositiveSmallIntegerField(
        choices=STARS_CHOICES,
        verbose_name='Оценка (звезды)'
    )

    is_approved = models.BooleanField(
        default=False
    )

    review = models.TextField(verbose_name='Текст отзыва')


    def __str__(self):
        return f'{self.author} - {self.stars}⭐'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'