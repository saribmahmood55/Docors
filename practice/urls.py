from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from practice import views

urlpatterns = [
    url(r'^physican/(?P<slug>[a-z-]+)$', views.practitioner, name='practitioner'),
    url(r'^physicans/(?P<speciality>[a-z-]+)-in-(?P<area>[a-z-]+)$', views.recentSearch, name='recentSearch'),
    url(r'^physicans', views.practitoners, name='practitoners'),
    url(r'^practice/(?P<practice_slug>[a-z-]+)/(?P<practitioner_slug>[a-z-]+)$', views.practice, name='practice'),
    url(r'^practice_hospitals/$', views.practice_hospitals, name='practice_hospitals'),
    url(r'^speciality/suggestions/$', views.speciality_suggestions, name='speciality_suggestions'),
    url(r'^practice/areas/$', views.get_areas, name='practice_areas'),
    url(r'^practice/initialreg/$', views.get_initial_reg, name='initial_reg_values')
]

urlpatterns = format_suffix_patterns(urlpatterns)