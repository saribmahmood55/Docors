from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from practice import views

urlpatterns = [
	url(r'^practices/$', views.PracticeList.as_view()),
	url(r'^practices/(?P<pk>[0-9]+)/$', views.PracticeDetail.as_view()),
    url(r'^physican/(?P<slug>[a-z-]+)$', views.practitioner, name='practitioner'),
    url(r'^physicans/(?P<speciality>[a-z-]+)-in-(?P<city>[a-z-]+)$', views.recentSearch, name='recentSearch'),
    url(r'^physicans', views.practitoners, name='practitoners'),
    url(r'^practice/(?P<practice_slug>[a-z-]+)/(?P<practitioner_slug>[a-z-]+)$', views.practice, name='practice'),
    url(r'^practice_hospitals/$', views.practice_hospitals, name='practice_hospitals'),
]

urlpatterns = format_suffix_patterns(urlpatterns)