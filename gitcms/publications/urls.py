from django.conf.urls.defaults import *
import settings
import views

urlpatterns = patterns('',
    (r'^publications/files/(?P<file>.+)$', 'django.views.static.serve', {'document_root': settings._BASE_DIR + '/../media/publications/files'}),
    (r'^publications/(?P<collection>.+)$', views.publications),
    (r'^publications$', views.publications, { 'collection' : 'luispedro' }),
)

