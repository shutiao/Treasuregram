from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
        path('', views.index),
        re_path(r'^([0-9]+)/$', views.detail, name = 'detail'),
        path('post_url/', views.post_treasure, name='post_treasure'),
        ]

if settings.DEBUG:
        urlpatterns += [
                re_path(r'^media/(?P<path>.*)$', serve,
                {'document_root': settings.MEDIA_ROOT,}),
        ]