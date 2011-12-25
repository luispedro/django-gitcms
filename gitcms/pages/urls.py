from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    (r'^tag/(?P<tag>.*)/?', views.bytag),
    (r'^(?P<url>.*)/?', views.article),
)
