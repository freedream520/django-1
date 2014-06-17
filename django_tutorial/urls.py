from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^posts/', include('posts.urls', namespace='posts')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django_tutorial.views.home', name='home'),
    url(r'^register/', 'django_tutorial.views.register', name='register'),
    url(r'^login/', 'django_tutorial.views.login_view', name='login'),
    url(r'^logout/', 'django_tutorial.views.logout_view', name='logout'),
    url(r'^user/(?P<user_id>\d+)/$', 'django_tutorial.views.user_page', name='user'),
    url(r'^user/(?P<user_id>\d+)/edit/$', 'django_tutorial.views.user_edit', name='edit_user'),
)
