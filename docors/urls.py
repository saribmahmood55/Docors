from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.auth.views import login, password_reset, password_reset_confirm, password_reset_done, password_reset_complete
from registration.backends.default.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail

class RegistrationViewUniqueEmail(RegistrationView):
    form_class = RegistrationFormUniqueEmail

urlpatterns = patterns('',
    url(r'^accounts/register', RegistrationViewUniqueEmail.as_view(),name='registration_register'),
    url(r'^social-accounts/', include('allauth.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^', include('practitioner.urls')),
    url(r'^', include('practice.urls')),
    url(r'^', include('patients.urls')),
    url(r'^', include('reviews.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^password/reset/$', 'django.contrib.auth.views.password_reset',{'post_reset_redirect' : '/password/reset/done/'}),
    url(r'^password/reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'post_reset_redirect' : '/password/done/'}),
    url(r'^password/done/$', 'django.contrib.auth.views.password_reset_complete'),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
    )
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
        )