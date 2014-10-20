from django.conf.urls import url, patterns
from patients import views

urlpatterns = patterns('',
    url(r'^patient', views.patient, name='patient'),
)