from django.contrib import admin


from .models.card import Card, CardPhoto, CardVideo, CardWorkDay
from .models.featured_card import FeaturedCard
from .models.location import Place
from .models.type import Type


admin.site.register(Place)


class CardVideoInline(admin.TabularInline):
    model = CardVideo
    extra = 3


class CardWorkDayInline(admin.TabularInline):
    model = CardWorkDay
    extra = 7


class CardPhotoInline(admin.TabularInline):
    model = CardPhoto
    extra = 3 


admin.site.register(Type)
admin.site.register(FeaturedCard)

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    inlines = [CardPhotoInline, CardVideoInline, CardWorkDayInline]
    list_display = ('id', 'title', 'category', 'phone_number') 
    search_fields = ('title', 'description')


@admin.register(CardPhoto)
class CardPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'card', 'image')
    search_fields = ('card__title',)


@admin.register(CardVideo)
class CardVideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'card', 'video')
    search_fields = ('card__title',)


@admin.register(CardWorkDay)
class CardWorkDayAdmin(admin.ModelAdmin):
    list_display = ('id', 'card', 'dayoftheweek', 'starts_work', 'stops_work')
    search_fields = ('card__title',)