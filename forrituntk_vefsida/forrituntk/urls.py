from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'forrituntk.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'forritun.views.index', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
