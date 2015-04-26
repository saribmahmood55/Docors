from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from patients import views

urlpatterns = [
	url(r'^accounts/login/$', views.custom_login),
	url(r'^patients/$', views.PatientList.as_view()),
	url(r'^patients/(?P<pk>[0-9]+)/$', views.PatientDetail.as_view()),
	url(r'^patient', views.patient, name='patient'),
	url(r'^subscribe/$', views.subscribe, name='subscribe'),
	url(r'^WhoIsMyDoctor', views.educate, name='WhoIsMyDoctor'),
	url(r'^dashboard/profile/$', views.profile),
	url(r'^dashboard/account/$', views.acc_preferences),
	url(r'^dashboard/specialities/$', views.dashboard_specialities)
]

urlpatterns = format_suffix_patterns(urlpatterns)