from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.contrib.auth.models import User

urlpatterns = patterns('',
    url(r'^', include('practitioner.urls')),
    url(r'^', include('patients.urls')),
    url(r'^', include('reviews.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('registration.backends.simple.urls')),
)