from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^tag/(?P<tag>.*)/?', views.bytag, name='simplecms-tag'),
    url(r'^(?P<url>.*)/?', views.article, name='simplecms'),
)
