from django.conf.urls import patterns, include, url

from posts import views

urlpatterns = patterns('',
  url(r'^new/$', views.new, name='new'),
  url(r'^(?P<post_id>\d+)/$', views.detail, name='detail'),
  url(r'^(?P<post_id>\d+)/delete/$', views.delete, name='delete'),
  url(r'^(?P<post_id>\d+)/edit/$', views.edit, name='edit'),
  url(r'^(?P<post_id>\d+)/comment/$', views.comment, name='comment'),
)
