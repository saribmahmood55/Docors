from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from practitioner.views import *


urlpatterns = patterns('',
    url(r'^docors/', include('practitioner.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
'''
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docors/', include('practitioner.urls')),
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
 
    #url(r'^practitioner_list/', practitioner.views.practitioners, name='practitioners'),
    #url(r'^(?P<question_id>[0-9]+)/$', practitioner.views.detail, name='detail'),
    #url(r'^docors/', 'practitioner.views.docors', name='docors'),
    #url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
'''
'''
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
'''
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
