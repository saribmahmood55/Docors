from django.conf.urls import url, patterns
from django.views.generic import RedirectView
from patients import views

urlpatterns = patterns('',
    url(r'^patient', views.patient, name='patient'),
    url(r'^review/(?P<review_id>\d+)/$', views.review, name='review'),
    url(r'^review', views.addReview, name='review'),
    
)