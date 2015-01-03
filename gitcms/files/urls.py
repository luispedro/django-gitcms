from django.conf.urls import patterns, url
import settings

urlpatterns = patterns('',
    url(r'^files/(?P<path>.+)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT + '/files'},
        name='files'),
)

