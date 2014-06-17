from django.conf.urls import patterns, include, url

from posts import views

urlpatterns = patterns('',
  url(r'^new/$', views.new, name='new'),
  url(r'^(?P<post_id>\d+)/$', views.detail, name='detail'),
)
