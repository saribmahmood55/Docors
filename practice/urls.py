from django.conf.urls import patterns, url
from practice import views

urlpatterns = patterns('',
    url(r'^physican/(?P<slug>[a-z-]+)$', views.practitioner, name='practitioner'),
    url(r'^physicans/(?P<speciality>[0-9A-Za-z-]+)-in-(?P<area>[0-9A-Za-z-]+)$', views.recentSearch, name='recentSearch'),
    url(r'^physicans/(?P<speciality>.+)-within-(?P<dist>.+)KM$', views.advSearch, name='advSearch'),
    url(r'^physicans', views.practitoners, name='practitoners'),
    url(r'^practice/(?P<practice_slug>[a-z-]+)/(?P<practitioner_slug>[a-z-]+)$', views.practice, name='practice'),
    url(r'^practice_hospitals/$', views.practice_hospitals, name='practice_hospitals'),
    url(r'^speciality/suggestions/$', views.speciality_suggestions, name='speciality_suggestions'),
    url(r'^practice/areas/$', views.get_areas, name='practice_areas'),
    url(r'^practice/initialreg/$', views.get_initial_reg, name='initial_reg_values'),
    url(r'^practice/advanced/$', views.advanced_search, name='advanced_search'),
)