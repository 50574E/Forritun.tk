from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    url(r'^$', 'forritun.views.index', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$',  login),
    url(r'^accounts/logout/$',  logout),
    url(r'^accounts/register/$',  'forritun.views.register'),
)
