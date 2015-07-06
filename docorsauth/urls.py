from django.conf.urls import patterns, url, include
from docorsauth import views

urlpatterns = patterns('',
    url('^accounts/register/$', views.register, name='registration_register'),
    #url('^accounts/login/$', views.custom_login, name='auth_login'),
    url('^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/accounts/login'}),
    url('^accounts/', include('django.contrib.auth.urls')),
)