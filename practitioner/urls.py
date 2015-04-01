from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from practitioner import views

urlpatterns = [
	url(r'^practitioners/$', views.PractitionerList.as_view()),
	url(r'^practitioners/(?P<pk>[0-9]+)/$', views.PractitionerDetail.as_view()),
	url(r'^$', views.index, name='index'),
	url(r'^adv', views.adv, name='adv'),
	url(r'^registration', views.registration, name='registration'),
]

urlpatterns = format_suffix_patterns(urlpatterns)