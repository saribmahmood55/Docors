from django.conf.urls import url, patterns
from practitioner import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^practitoners', views.practitoners, name='practitoners'),
    url(r'^practitioner/(?P<slug>[a-z-]+)/$', views.practitioner, name='practitioner'),
    url(r'^registration', views.registration, name='registration'),
)