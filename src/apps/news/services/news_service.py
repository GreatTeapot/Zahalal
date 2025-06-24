from apps.news.models.news import NewsPost


def get_all_news_posts():
    return NewsPost.objects.all()


def get_news_post_by_id(post_id: int):
    return NewsPost.objects.prefetch_related('photos', 'videos').get(id=post_id)