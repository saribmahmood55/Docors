from django.conf.urls import url, patterns
from django.views.generic import RedirectView
from patients import views

urlpatterns = patterns('',
    url(r'^patient', views.patient, name='patient'),
    url(r'^addreview', views.addreview, name='addreview'),
    url(r'^review/(?P<review_id>\d+)/$', views.review, name='review'),
)