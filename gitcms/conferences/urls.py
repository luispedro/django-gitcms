from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    url(r'^conferences/?$', views.upcoming, name='conferences-index'),
    url(r'^conferences/upcoming/?$', views.upcoming, name='conferences-upcoming'),
    url(r'^conferences/upcoming/ical', views.upcomingical, name='conferences-ical'),
    url(r'^conferences/upcoming-submissions', views.upcoming_submissions, name='conferences-submissions'),
)
