from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

import session_csrf
session_csrf.monkeypatch()

from django.contrib import admin
admin.autodiscover()

from scout.properties import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home_view, name='home'),

    url(r'^markers/', include('scout.markers.urls', namespace='markers')),
    url(r'^properties/', include('scout.properties.urls', namespace='properties')),

    url(r'^_ah/', include('djangae.urls')),

    # Note that by default this is also locked down with login:admin in app.yaml
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('djangae.contrib.gauth.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)