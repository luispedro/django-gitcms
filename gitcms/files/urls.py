from django.conf.urls.defaults import *
import settings

urlpatterns = patterns('',
    (r'^files/(?P<path>.+)$', 'django.views.static.serve', {'document_root': settings._BASE_DIR + '/../media/files'}),
)

