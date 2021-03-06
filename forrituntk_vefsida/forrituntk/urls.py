from django.conf.urls import patterns, include, url
from django.contrib import admin
from forritun.views import ProgrammingLanguageListView, ResourceListView
from discourse import views

urlpatterns = patterns('',
    url(r'^$', 'forritun.views.index', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$',  'forritun.views.login_view', name='login-view'),
    url(r'^accounts/logout/$',  'forritun.views.logout_view', name='logout-view'),
    url(r'^accounts/register/$',  'forritun.views.register', name='register-view'),
    url(r'^languages/$', ProgrammingLanguageListView.as_view(), name='language-list'),
    url(r'^languages/(?P<id>\d+)/(?P<slug>[-\w\d]*)/(?P<tags>[-+\w\d]*)?$', ResourceListView.as_view(), name='resource-list'),
    url(r'^discourse/sso$', views.sso),
)
