from django.conf.urls import patterns, url

from scout.markers import views

urlpatterns = patterns(
    '',
    url(r'^add/$', views.marker_add_view, name='add'),
)
