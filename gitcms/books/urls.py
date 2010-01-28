from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    (r'^(?P<url>.*)/?', views.book),
)
