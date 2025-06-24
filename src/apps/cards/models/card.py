from django.db import models
from common.models.base import BaseModel


class Card(BaseModel):
    """
    Модель Карточки заведения.

    Аттрибуты:
    - face_img: главное фото
    - whatsapp: ссылка на WhatsApp
    - telegram: ссылка на Telegram
    - site: ссылка на сайт
    - description: описание
    - location: ссылка на локацию
    - category: категория
    - title: название заведения
    - address: полный адрес
    - type: тип заведения
    - city: город заведения
    """


    face_img = models.ImageField(
        upload_to='media/cards/faces/',
        verbose_name='Главное фото'
    )

    type = models.ForeignKey(
        to='cards.Type',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='cards',
        verbose_name='Тип заведения'
    )
     
    address = models.CharField(
        max_length=255,
        verbose_name='Полный адрес',
        help_text='Например: г. Бишкек, ул. Ленина, 25'
    ) 

    city = models.CharField(
    max_length=100,
    verbose_name='Город',
    help_text='Например: Бишкек',
    blank=True,
    null=True
    )

    title = models.CharField(
        max_length=100,
        verbose_name='Название заведения'
    )

    category = models.ForeignKey(
    to='categories.Category',
    on_delete=models.CASCADE,
    null=True,
    blank=True,
    related_name='cards',
    verbose_name='Категория',
    )   

    phone_number = models.CharField(
    max_length=20,
    verbose_name='Номер телефона',
    help_text='Например: +996707123456',
    blank=True,
    null=True
    )

    whatsapp = models.URLField(
        blank=True,
        null=True,
        verbose_name='Ссылка на WhatsApp'
    )

    telegram = models.URLField(
        blank=True,
        null=True,
        verbose_name='Ссылка на Telegram'
    )

    site = models.URLField(
        blank=True,
        null=True,
        verbose_name='Сайт'
    )

    description = models.TextField(
        verbose_name='Описание'
    )

    location = models.ForeignKey(
        'cards.Place',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='cards',
        verbose_name='Локация'
    )

    def __str__(self):
        return f'{self.description[:30]}...'

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'


class CardPhoto(BaseModel):
    """
    Модель дополнительных фотографий заведения
    """
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='photos', verbose_name='Карточка')
    image = models.ImageField(upload_to='media/cards/photos/', verbose_name='Фото')

    def __str__(self):
        return f'Фото для {self.card}'
    
    class Meta:
        verbose_name = 'Фото заведения'
        verbose_name_plural = 'Фотки заведения'


class CardVideo(BaseModel):
    """
    Модель дополнительных видео заведения
    """
    card = models.ForeignKey(
        Card,
        on_delete=models.CASCADE,
        related_name='videos',
        verbose_name='Карточка'
    )
    video = models.FileField(
        upload_to='media/cards/videos/',
        verbose_name='Видео'
    )

    def __str__(self):
        return f'Видео для {self.card}'
    
    class Meta:
        verbose_name = 'Видео заведения'
        verbose_name_plural = 'Видео заведения'


class CardWorkDay(BaseModel):
    """
    Модель дней работы заведения
    """

    DAYSOFTHEWEEK = (
        ('Monday', 'Понедельник'),
        ('Tuesday', 'Вторник'),
        ('Wednesday', 'Среда'),
        ('Thursday', 'Четверг'),
        ('Friday', 'Пятница'),
        ('Saturday', 'Суббота'),
        ('Sunday', 'Воскресенье'),
    )

    card = models.ForeignKey(
        Card,
        on_delete=models.CASCADE,
        related_name='work_days',
        verbose_name='Карточка'
    )

    dayoftheweek = models.CharField(
        max_length=10,
        choices=DAYSOFTHEWEEK,
        verbose_name='День недели'
    )

    starts_work = models.TimeField(
        verbose_name='Время открытия'
    )

    stops_work = models.TimeField(
        verbose_name='Время закрытия'
    )


    def __str__(self):
        return f'День работы для {self.card}'


    class Meta:
        verbose_name = 'День работы'
        verbose_name_plural = 'Дни работы'