from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf.urls.static import static
from config import settings

urlpatterns = [
    path('super-secure-admin-panel/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('cards/', include('apps.cards.urls')),
    path('reviews/', include('apps.reviews.urls')),
    path('categories/', include('apps.categories.urls')),
    path('news/', include('apps.news.urls')),
]




urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
