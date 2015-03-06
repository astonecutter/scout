from django.conf.urls import patterns, url

from scout.sharing import views


urlpatterns = patterns(
    '',
    url(r'^$', views.user_list_view, name='list'),
    url(r'^add/$', views.user_add_view, name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.user_edit_view, name='edit'),
)