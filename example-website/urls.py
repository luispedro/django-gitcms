from . import settings
from django.conf.urls import patterns, url, include
from django.contrib import admin
import gitcms.pages.urls
import gitcms.files.urls
import gitcms.blog.urls
admin.autodiscover()

urlpatterns = patterns('',
    (r'^media/(?P<path>.+)$', 'django.views.static.serve', {'document_root': settings._BASE_DIR + '/media'}),
    (r'^admin/', include(admin.site.urls)),
    (r'^blog/?', include(gitcms.blog.urls)),
)
urlpatterns += gitcms.files.urls.urlpatterns
urlpatterns += gitcms.pages.urls.urlpatterns

