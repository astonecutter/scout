from django.conf.urls import patterns, url

from scout.properties import views


urlpatterns = patterns(
    '',
    url(r'^add/$', views.property_add_view, name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.property_edit_view, name='edit'),
)