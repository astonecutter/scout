from django.conf.urls import patterns, include, url

import session_csrf
session_csrf.monkeypatch()

from django.contrib import admin
admin.autodiscover()

from scout import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home_view, name='home'),
    url(r'^add/$', views.add_view, name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit_view, name='edit'),
    url(r'^_ah/', include('djangae.urls')),

    # Note that by default this is also locked down with login:admin in app.yaml
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('djangae.contrib.gauth.urls')),
)