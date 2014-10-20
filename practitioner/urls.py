from django.conf.urls import url, patterns
from practitioner import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^q', views.q, name='q'),
    url(r'^practitioner/(?P<slug>[a-z-]+)/$', views.practitioner, name='practitioner'),
    url(r'^register', views.register, name='register'),
)