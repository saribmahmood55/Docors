from django.conf.urls import patterns, url
from patients import views

urlpatterns = patterns('',
	url(r'^patient', views.patient, name='patient'),
	url(r'^subscribe/$', views.subscribe, name='subscribe'),
	url(r'^WhoIsMyDoctor', views.educate, name='WhoIsMyDoctor'),
	url(r'^favt_pract', views.favt_pract, name='add_favt_pract'),
	url(r'^dashboard/profile/$', views.profile),
	url(r'^dashboard/account/$', views.acc_preferences),
	url(r'^dashboard/specialities/$', views.dashboard_specialities)
)