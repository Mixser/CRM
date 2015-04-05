from django.conf.urls import patterns, include, url
from base.views import HomeView, EmployerUpdateView, ScheduleView, EventUpdateView

urlpatterns = patterns('base.views',

                       url(r'^/?$', HomeView.as_view(), name='home'),
                       url(r'^schedule/?$', ScheduleView.as_view(), name='schedule'),

                       url(r'^event/(?P<pk>[0-9]+)/edit/?$', EventUpdateView.as_view() , name='event_update'),

                       url(r'employer/(?P<pk>[0-9]+)/$', EmployerUpdateView.as_view(), name='employer_update'),

                       )