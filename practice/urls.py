from django.conf.urls import url, patterns
from practice import views

urlpatterns = patterns('',
	url(r'^search$', views.practitioner_name, name='practitioner_name'),
    url(r'^physican/(?P<slug>[a-z-]+)$', views.practitioner, name='practitioner'),
    url(r'^physicans/(?P<speciality>[a-z-]+)-in-(?P<city>[a-z-]+)$', views.recentSearch, name='recentSearch'),
    url(r'^physicans', views.practitoners, name='practitoners'),
    url(r'^practice/(?P<practice_slug>[a-z-]+)/(?P<practitioner_slug>[a-z-]+)$', views.practice, name='practice'),
    )