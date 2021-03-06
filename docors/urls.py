#flake8: noqa
from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth.views import login, password_reset
from django.contrib.auth.views import password_reset_confirm, password_reset_done
from django.contrib.auth.views import password_reset_complete
from docors import views
from practitioner.sitemap import PractitionerSitemap

sitemaps = {
    'practitioners': PractitionerSitemap,
}

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^adv', views.adv, name='adv'),
    url(r'^social-accounts/', include('allauth.urls')),
    url(r'^', include('docorsauth.urls')),
    url(r'^', include('practitioner.urls')),
    url(r'^', include('practice.urls')),
    url(r'^', include('patients.urls')),
    url(r'^', include('reviews.urls')),
    url(r'hitcount/', include('hitcount.urls', namespace='hitcount')),
    url(r'^search/', include('haystack.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^password/reset/$', 'django.contrib.auth.views.password_reset',{'post_reset_redirect' : '/password/reset/done/'}, name='password_reset'),
    url(r'^password/reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'post_reset_redirect' : '/password/done/'}),
    url(r'^password/done/$', 'django.contrib.auth.views.password_reset_complete'),
    url(r'^privacy-policy/$', views.policy, name='privacy_policy'),
    url(r'^terms-service/$', views.tos, name='tos'),
    url(r'^user-agreement/$', views.user_agreement, name='user_agreement'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
    )
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
        )