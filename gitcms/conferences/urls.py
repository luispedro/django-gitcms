from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    (r'^conferences/?$', views.upcoming),
    (r'^conferences/upcoming/?$', views.upcoming),
    (r'^conferences/upcoming/ical', views.upcomingical),
    (r'^conferences/upcoming-submissions', views.upcoming_submissions),
)
