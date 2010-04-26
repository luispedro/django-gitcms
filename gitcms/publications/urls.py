from django.conf.urls.defaults import *
import settings
import views

urlpatterns = patterns('',
    (r'^papers/(?P<paper>.+)$', views.papers),
    (r'^publications/?$', views.publications, { 'collection' : 'luispedro' }),
    (r'^publications/(?P<collection>.+)$', views.publications),
    (r'^publications/files/(?P<file>.+)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT + '/publications/files'}),
)

