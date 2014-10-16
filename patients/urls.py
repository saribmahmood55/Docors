from django.conf.urls import url, patterns 
from patients import views

urlpatterns = patterns('',
    url(r'^patient/', views.patient, name='patient'),
    url(r'^addReview/', views.addReview, name='addReview'),
    url(r'^up/(?P<practitionerreview_id>\d+)/$', views.patient, name='up'),
    url(r'^down/(?P<practitionerreview_id>\d+)/$', views.patient, name='down'),
)