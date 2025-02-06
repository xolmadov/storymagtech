from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    
    path('', popular_news, name='popular_news'),
    path('news/<int:news_id>/', news_detail, name='news_detail'),
    path('gadget/<int:gadget_id>/', gadget_detail, name='gadget_detail'),
    path('latest/<int:latest_id>/', lt_detail, name='lt_detail'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
