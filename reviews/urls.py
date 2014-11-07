from django.conf.urls import url, patterns
from django.views.generic import RedirectView
from reviews import views

urlpatterns = patterns('',
	url(r'^review', views.addReview, name='addreview'),
    url(r'^review/(?P<review_id>\d+)/$', views.review, name='review'),
)