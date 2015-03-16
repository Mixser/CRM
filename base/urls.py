from django.conf.urls import patterns, include, url


urlpatterns = patterns('base.views', 
    url(r'^home/?$', 'home', name='home'),
    ) 