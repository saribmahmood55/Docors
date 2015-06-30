from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from patients import views

urlpatterns = [
	url(r'^accounts/login/$', views.custom_login),
	url(r'^patient', views.patient, name='patient'),
	url(r'^subscribe/$', views.subscribe, name='subscribe'),
	url(r'^WhoIsMyDoctor', views.educate, name='WhoIsMyDoctor'),
	url(r'^favt_pract', views.favt_pract, name='add_favt_pract'),
	url(r'^dashboard/profile/$', views.profile),
	url(r'^dashboard/account/$', views.acc_preferences),
	url(r'^dashboard/specialities/$', views.dashboard_specialities)
]

urlpatterns = format_suffix_patterns(urlpatterns)