from django.conf.urls import patterns, url
from patients import views

urlpatterns = patterns('',
	url(r'^patient/physican', views.physican_patient, name='patient_physican'),
	url(r'^patient/specialities', views.specialities_patient, name='patient_specialty'),
	url(r'^patient/reviews', views.reviews_patient, name='patient_reviews'),
	url(r'^patient/profile', views.profile_patient, name='patient_profile'),
	url(r'^patient/subscribe', views.subscribe_patient, name='subscribe'),
	url(r'^WhoIsMyDoctor', views.educate_patient, name='WhoIsMyDoctor'),
	url(r'^favt_pract', views.favt_pract, name='add_favt_pract'),
	url(r'^patient/preferences/$', views.preferences_patient, name='patient_preferences'),
)
