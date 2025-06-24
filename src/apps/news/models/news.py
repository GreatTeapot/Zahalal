from django.db import models
from common.models.base import BaseModel


class NewsPost(BaseModel):
    face_image = models.ImageField(upload_to='news/face_images/')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class PostPhoto(BaseModel):
    post = models.ForeignKey(NewsPost, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news/photos/')


class PostVideo(BaseModel):
    post = models.ForeignKey(NewsPost, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='news/videos/')