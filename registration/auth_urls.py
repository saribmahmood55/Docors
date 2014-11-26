from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth import views as auth_views


urlpatterns = patterns('',
  url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='auth_login'),
  url(r'^logout/$', auth_views.logout,  {'next_page': '/'}, name='auth_logout'),
  url(r'^password/change/$', auth_views.password_change, {'post_change_redirect': reverse_lazy('auth_password_change_done')},name='auth_password_change'),
  url(r'^password/change/done/$', auth_views.password_change_done, name='auth_password_change_done'),
  url(r'^password/reset/$', 'django.contrib.auth.views.password_reset',{'post_reset_redirect': reverse_lazy('auth_password_reset_done')}, name='auth_password_reset'),
  url(r'^password/reset/confirm/$', 'django.contrib.auth.views.password_reset_confirm'),
  url(r'^password/reset/complete/$', 'django.contrib.auth.views.password_reset_complete'),
  url(r'^password/reset/done/$', auth_views.password_reset_done, name='auth_password_reset_done'),
)