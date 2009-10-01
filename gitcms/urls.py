from django.conf.urls.defaults import *
from django.contrib import admin
import simplecms.urls
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
)
urlpatterns += simplecms.urls.urlpatterns
