from django.db import models
from common.models.base import BaseModel


class Type(BaseModel):
    """
    Модель типов карточек
    """
    type = models.CharField(
        max_length=50,
        verbose_name='Тип заведения',
    )

    def __str__(self):
        return self.type
    
    class Meta:
        verbose_name = 'Тип заведения'
        verbose_name_plural = 'Типы заведений'