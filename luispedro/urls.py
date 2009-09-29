from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^luispedro/', include('luispedro.foo.urls')),

    (r'^admin/', include(admin.site.urls)),
)
