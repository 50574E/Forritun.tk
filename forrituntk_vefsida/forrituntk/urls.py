from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from forritun.views import ProgrammingLanguageListView, ResourceListView
from discourse import views

urlpatterns = patterns('',
    url(r'^$', 'forritun.views.index', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$',  login),
    url(r'^accounts/logout/$',  logout),
    url(r'^accounts/register/$',  'forritun.views.register'),
    url(r'^languages/$', ProgrammingLanguageListView.as_view(), name='language-list'),
    url(r'^languages/(?P<id>\d+)/(?P<slug>[-\w\d]+)/$', ResourceListView.as_view(), name='resource-list'),
    url(r'^discourse/sso$', views.sso),
)
