from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    (r'^articles/(?P<slug>[-a-zA-Z0-9]+)', views.article),
)
