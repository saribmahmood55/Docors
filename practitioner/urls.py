from django.conf.urls import url, patterns 
from practitioner import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search, name='search'),
    url(r'^practitioner/(?P<slug>[a-z-]+)/$', views.practitioner, name='practitioner'),
)