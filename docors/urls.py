from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


urlpatterns = patterns('',
    url(r'^', include('practitioner.urls')),
    url(r'^', include('patients.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('registration.backends.simple.urls')),
)
'''
    #url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
'''

