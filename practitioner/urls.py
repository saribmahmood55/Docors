#flake8: noqa
from django.conf.urls import patterns, url
from practitioner import views

urlpatterns = patterns('',
  #Search Related urls
  url(r'^physican/suggestions/$', views.suggestions_practitioner, name='physican_suggestions'),
  url(r'^physican/search/$', views.search_practitioner, name='physican_search'),
  url(r'^(?P<slug>[a-z-]+)-in-(?P<typee>[A-Za-z-]+)$', views.results_practitioner, name='physican_results'),
  #Physican Page urls
  url(r'^physican/(?P<slug>[\w-]+)/claim/$', views.claim_practitioner, name='claim_practitioner'),
  url(r'^physican/(?P<slug>[\w-]+)/update/info/$', views.update_info_practitioner, name='update_info_practitioner'),
  url(r'^physican/(?P<slug>[\w-]+)/profile/$', views.profile_practitioner, name='practitioner_profile'),
  url(r'^physican/(?P<slug>[\w-]+)/review/$', views.review_practitioner, name='practitioner_review'),
  #Physican Registration related urls
  url(r'^physican/registration', views.registration_practitioner, name='practitioner_registration'),
  url(r'^physican/get-cond-proc-ajax/$', views.get_cond_proc_ajax, name='get_condition_procedure'),
  url(r'^physican/get-practice-names-ajax/$', views.get_practice_names_ajax, name='get_practice_names'),
  url(r'^physican/get-practice-details-ajax/$', views.get_practice_details_ajax, name='get_practice_details'),
  )
