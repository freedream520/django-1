from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django_tutorial.views.home', name='home'),
    url(r'^register/', 'django_tutorial.views.register', name='register'),
    url(r'^login/', 'django_tutorial.views.login_view', name='login'),
)
