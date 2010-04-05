from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    (r'^tag/(?P<tag>.*)/?', views.bytag),
    (r'^(?P<year>[0-9]+)/(?P<month>[^/]*)/(<?P<slug>[^/]*)/?', views.post),
    (r'^/?', views.mostrecent),
)
