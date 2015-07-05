from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from practitioner import views

urlpatterns = [
	url(r'^physicans-directory/(?P<slug>[a-z-]+)-in-(?P<typee>[a-z-]+)$', views.practitionerSearch, name='practitionerSearch'),
	url(r'^practitioner/registration', views.registration, name='registration'),
	url(r'^practitioner/suggestions/$', views.practitioner_suggestions, name='doctor_suggestions'),
	url(r'^practitioner/getCondProc/$', views.get_condition_procedure, name='get_condition_procedure'),
	url(r'^practitioner-search/$', views.get_search_practitioner, name='get_search_practitioner')
]

urlpatterns = format_suffix_patterns(urlpatterns)