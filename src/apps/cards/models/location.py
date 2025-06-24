from django.db import models

class Place(models.Model):
    """
    Модель локации.

    Аттрибуты:
    - name: название места
    - latitude: широта
    - longitude: долгота
    """
    name = models.CharField(
        max_length=100, 
        verbose_name="Название места"
    )

    latitude = models.FloatField(
        verbose_name="Широта"
    )

    longitude = models.FloatField(
        verbose_name="Долгота"
    )
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"