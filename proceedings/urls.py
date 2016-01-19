from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', 'proceedings.views.home', name='proceedings'),
    url(r'^(?P<key>[-\w\. ]+)/$', 'proceedings.views.home', name='proceedings-alltag'),
)
