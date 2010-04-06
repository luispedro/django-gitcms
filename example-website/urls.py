import settings
from django.conf.urls.defaults import *
from django.contrib import admin
import gitcms.simplecms.urls
import gitcms.files.urls
import gitcms.blog.urls
admin.autodiscover()

urlpatterns = patterns('',
    (r'^media/(?P<path>.+)$', 'django.views.static.serve', {'document_root': settings._BASE_DIR + '/media'}),
    (r'^admin/', include(admin.site.urls)),
)
urlpatterns += gitcms.blog.urls.urlpatterns
urlpatterns += gitcms.files.urls.urlpatterns
urlpatterns += gitcms.simplecms.urls.urlpatterns

