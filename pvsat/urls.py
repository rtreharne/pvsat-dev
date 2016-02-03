from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', 'pvsat.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^programme/', include('programme.urls')),
    url(r'^registration/$', 'programme.views.registration', name='registration'),
    url(r'^committee/', include('committee.urls')),
    url(r'^authors/', include('authors.urls')),
	url(r'^contact/', include('message.urls')),
	url(r'^venue/', include('venue.urls')),
	url(r'^bursary/', include('bursary.urls')),
	gurl(r'^proceedings/', include('proceedings.urls')),
)

urlpatterns += patterns(
    'django.views.static',
    (r'^media/(?P<path>.*)',
    'serve',
    {'document_root': settings.MEDIA_ROOT}),
                )

urlpatterns = patterns('',
    url(r'^favicon.ico/$', lambda x: HttpResponseRedirect(settings.STATIC_URL+'img/favicon.ico')), #google chrome favicon fix
)
