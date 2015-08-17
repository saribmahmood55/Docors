from django.conf.urls import patterns, url
from practice import views

urlpatterns = patterns('',
                       #Search by sepcialty
                       url(r'^practice/speciality/$', views.search_specialty, name='search_speciality'),
                       url(r'^(?P<speciality>[0-9A-Za-z-]+)-in-(?P<area>[0-9A-Za-z-]+)$', views.results_specialty, name='results_specialty'),
                       #Advanced Radius Search
                       url(r'^practice/advanced/$', views.search_advanced, name='search_advanced'),
                       url(r'^(?P<speciality>.+)-within-(?P<dist>.+)KM$', views.results_advanced, name='results_advanced'),
                       url(r'^physican/(?P<slug>[\w-]+)/$', views.practitioner, name='practitioner'),
                       url(r'^practice/get-areas-ajax/$', views.get_areas_ajax, name='get_areas'),
                       )
