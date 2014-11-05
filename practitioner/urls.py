from django.conf.urls import url, patterns
from practitioner import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^adv', views.adv, name='adv'),
	url(r'^registration', views.registration, name='registration'),
    url(r'^update', views.update, name="update"),
)