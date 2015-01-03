from django.conf.urls import patterns, url
from . import views
from . import feeds


urlpatterns = patterns('',
    url(r'^tag/(?P<tag>.*)/', views.bytag, name='blog-tag'),
    url(r'^(?P<year>[0-9]+)/(?P<month>[0-9]+)/(?P<slug>[^/]*)/', views.post, name='blog-post'),
    url(r'^feed/', feeds.LatestFeed(), name='blog-feed'),
    url(r'^/?$', views.mostrecent, name='blog'),
)
