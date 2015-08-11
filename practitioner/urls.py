from django.conf.urls import patterns, url
from practitioner import views

urlpatterns = patterns('',
                       url(r'^physicans-directory/(?P<slug>[a-z-]+)-in-(?P<typee>[a-z-]+)$', views.practitionerSearch, name='practitionerSearch'),
                       url(r'^practitioner/registration', views.registration, name='registration'),
                       url(r'^practitioner/suggestions/$', views.practitioner_suggestions, name='doctor_suggestions'),
                       url(r'^practitioner/getCondProc/$', views.get_condition_procedure, name='get_condition_procedure'),
                       url(r'^practitioner/get-practice-names/$', views.get_practice_names, name='get_practice_names'),
                       url(r'^practitioner/get-practice-details/$', views.get_practice_details, name='get_practice_details'),
                       url(r'^practitioner-search/$', views.get_search_practitioner, name='get_search_practitioner'),
                       url(r'^physican/(?P<slug>[a-z-]+)/claim/$', views.claim_practitioner, name='claim_practitioner'),
                       url(r'^physican/(?P<slug>[a-z-]+)/update/info/$', views.update_info_practitioner, name='update_info_practitioner'),
                       url(r'^physican/(?P<slug>[a-z-]+)/profile/$', views.profile, name='practitioner_profile'),
                       )
