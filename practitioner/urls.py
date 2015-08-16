from django.conf.urls import patterns, url
from practitioner import views

urlpatterns = patterns('',
                       url(r'^physicans-directory/(?P<slug>[a-z-]+)-in-(?P<typee>[A-Za-z-]+)$', views.practitionerSearch, name='practitionerSearch'),
                       url(r'^practice-search/(?P<slug>[a-z-]+)-in-(?P<typee>[A-Za-z-]+)$', views.practice_search, name='practice_search'),
                       url(r'^practitioner/registration', views.registration, name='registration'),
                       url(r'^practitioner/suggestions/$', views.practitioner_suggestions, name='doctor_suggestions'),
                       url(r'^practitioner/getCondProc/$', views.get_condition_procedure, name='get_condition_procedure'),
                       url(r'^practitioner/get-practice-names/$', views.get_practice_names, name='get_practice_names'),
                       url(r'^practitioner/get-practice-details/$', views.get_practice_details, name='get_practice_details'),
                       url(r'^practitioner-search/$', views.get_search_practitioner, name='get_search_practitioner'),
                       url(r'^practice-search/$', views.get_search_practice, name='get_search_practice'),
                       url(r'^physican/(?P<slug>[\w-]+)/claim/$', views.claim_practitioner, name='claim_practitioner'),
                       url(r'^physican/(?P<slug>[\w-]+)/update/info/$', views.update_info_practitioner, name='update_info_practitioner'),
                       url(r'^physican/(?P<slug>[\w-]+)/profile/$', views.profile, name='practitioner_profile'),
                       url(r'^physican/(?P<slug>[\w-]+)/review/$', views.new_review, name='practitioner_review'),
                       )
