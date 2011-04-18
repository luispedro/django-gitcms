from django.conf.urls.defaults import *
import settings
import views


urlpatterns = patterns('',
    url(r'^papers/(?P<paper>.+)$', views.papers, name='publications-paper'),
    url(r'^publications/?$', views.publications, {'collection' : 'luispedro'}, name='publications'),
    url(r'^publications/(?P<collection>.+)$', views.publications, name='publications-collection'),
    url(r'^publications/files/(?P<file>.+)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT + '/publications/files'}, name='publications-files'),
)
