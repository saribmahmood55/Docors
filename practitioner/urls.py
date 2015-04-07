from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from practitioner import views

urlpatterns = [
	url(r'^practitioners/$', views.PractitionerList.as_view()),
	url(r'^practitioner-title/$', views.PractitionerTileList.as_view()),
	url(r'^practitioners/(?P<pk>[0-9]+)/$', views.PractitionerDetail.as_view()),
	url(r'^specializations/$', views.SpecializationList.as_view()),
	url(r'^specializations/(?P<pk>[0-9]+)/$', views.SpecializationDetail.as_view()),
	url(r'^degrees/$', views.DegreeList.as_view()),
	url(r'^degrees/(?P<pk>[0-9]+)/$', views.DegreeDetail.as_view()),
	url(r'^physiciantypes/$', views.PhysicianTypeList.as_view()),
	url(r'^physiciantitles/$', views.PhysicianTitleList.as_view()),
	url(r'^physiciangenders/$', views.PhysicianGenderList.as_view()),
	url(r'^$', views.index, name='index'),
	url(r'^adv', views.adv, name='adv'),
	url(r'^registration', views.registration, name='registration'),
]

urlpatterns = format_suffix_patterns(urlpatterns)