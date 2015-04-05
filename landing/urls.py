from django.conf.urls import patterns, include, url
from landing.views import SignInView, SignOutView, LandingView

urlpatterns = patterns('base.views',

                       url(r'^signin/?$', SignInView.as_view(), name='signin'),
                       url(r'^signout/?$', SignOutView.as_view(), name='signout'),

                       url(r'^/?$', LandingView.as_view(), name='landing')

                       # url(r'^schedule/?$', 'hh', name='schedule'),
)