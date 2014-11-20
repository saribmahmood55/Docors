from django.conf.urls import url, patterns
from patients import views

urlpatterns = patterns('',
	url(r'^patient', views.patient, name='patient'),
	url(r'^subscribe/$', views.subscribe, name='subscribe'),
)