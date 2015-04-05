from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
           url(r'^grappelli/', include('grappelli.urls')),
           url(r'^admin/', include(admin.site.urls)),
           url(r'^dashboard/', include('base.urls')),
           url(r'^', include('landing.urls')),
)