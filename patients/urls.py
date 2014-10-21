from django.conf.urls import url, patterns
from patients import views

urlpatterns = patterns('',
    url(r'^patient', views.patient, name='patient'),
    url(r'^review/(?P<review_id>\d+)/$', views.review, name='review'),
)