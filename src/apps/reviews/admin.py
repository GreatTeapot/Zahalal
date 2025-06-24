from django.contrib import admin
from .models.review import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'card', 'stars', 'created_at')
    search_fields = ('author__username', 'card__description')
    list_filter = ('stars',)