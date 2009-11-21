from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    (r'^category/(?P<category>.*)/?', views.bycategory),
    (r'^(?P<url>.*)/?', views.article),
)
