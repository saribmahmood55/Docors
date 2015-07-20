# flake8: noqa
from django.conf.urls import patterns, url, include
from docorsauth import views

urlpatterns = patterns('',
    url(r'^accounts/register/$', views.register, name='registration_register'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': 'index'}),
    url(r'^accounts/activate/(?P<token>.+)/$', views.activate, name='activate_account'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
)