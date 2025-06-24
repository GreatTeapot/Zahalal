from rest_framework import serializers
from apps.news.models.news import NewsPost, PostPhoto, PostVideo


class NewsPostShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPost
        fields = ['id', 'title', 'face_image', 'description']


class PostPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPhoto
        fields = ['id', 'image']


class PostVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostVideo
        fields = ['id', 'video']


class NewsPostFullSerializer(serializers.ModelSerializer):
    photos = PostPhotoSerializer(many=True, read_only=True)
    videos = PostVideoSerializer(many=True, read_only=True)

    class Meta:
        model = NewsPost
        fields = ['id', 'title', 'face_image', 'description', 'photos', 'videos']