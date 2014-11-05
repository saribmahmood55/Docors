from django.conf.urls import url, patterns
from practice import views

urlpatterns = patterns('',
    url(r'^practitoners', views.practitoners, name='practitoners'),
    url(r'^practitioner/(?P<slug>[a-z-]+)/$', views.practitioner, name='practitioner'),
    url(r'^practice/(?P<practice_slug>[a-z-]+)/(?P<practitioner_slug>[a-z-]+)/$', views.practice, name='practice'),
    )