from django.contrib import admin
from apps.news.models.news import NewsPost, PostPhoto, PostVideo


class PostPhotoInline(admin.TabularInline):
    model = PostPhoto
    extra = 2


class PostVideoInline(admin.TabularInline):
    model = PostVideo
    extra = 2


@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    inlines = [PostPhotoInline, PostVideoInline]
    list_display = ('id', 'title', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')