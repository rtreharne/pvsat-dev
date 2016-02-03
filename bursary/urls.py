from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', 'bursary.views.overview', name='overview'),
    url(r'^supersolar/$', 'bursary.views.application', name='application'),
)
