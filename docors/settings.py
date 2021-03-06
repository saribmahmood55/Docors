# flake8: noqa
from django.conf import global_settings
import os, socket, sys

boolean = lambda value: bool(int(value))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zky%mapoo709@yv64h!ny#!7x8#&lh0o9nsfo++ny6+7gotp^r'

# SECURITY WARNING: don't run with debug turned on in production!

if socket.gethostname() == 'asad-Inspiron-N5110' or socket.gethostname() == 'sarib-Inspiron-N5110':
    DEBUG = boolean(os.environ.get('DEBUG', 1))
else:
    DEBUG = boolean(os.environ.get('DEBUG', 0))
    SEND_BROKEN_LINK_EMAILS = True

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Asad Naeem', 'doctorsinfo.pk@gmail.com'),
)

MANAGERS = (
    ('Sarib Mehmood', 'saribmahmood55@gmail.com'),
)
MANAGERS = ADMINS
#Celery configuration

# using serializer name
CELERY_ACCEPT_CONTENT = [u'application/json',u'application/x-python-serialize',u'json']
BROKER_URL = 'amqp://asadnaeem:asad0321@localhost:5672/vir_host'
CELERY_TIMEZONE = 'Asia/Karachi'
CELERY_ENABLE_UTC = True
CELERY_IGNORE_RESULT = False
#BROKER_URL = 'amqp://%(proj_name)s:%(admin_pass)s@127.0.0.1:5672/%(proj_name)s'

#google recaptcha
RECAPTCHA_PUBLIC_KEY = '6LcAdv4SAAAAAI2hi_VgcifchYmJFUNmxdfajJJO'
RECAPTCHA_PRIVATE_KEY = '6LcAdv4SAAAAADhfTOFq09BVM8Kmi_15Go9v2caw'
RECAPTCHA_USE_SSL = False

#Security params
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True

#CUSTOM AUTH Backend
AUTH_USER_MODEL = 'docorsauth.docorsUser'

#Sites
SITE_ID = 2

#BASE URL
BASE_URL = "http://localhost:8000/"

#Support Email SMPTP
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'support@doctorsinfo.pk'
EMAIL_HOST_PASSWORD = 'g3zcehxgx3cb'
EMAIL_HOST_USER = 'support@doctorsinfo.pk'

#haystack
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}


# Application definition
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.gis',
    'django.contrib.sitemaps',
    'docorsauth',
    'haystack',
    #'registration',
    'sorl.thumbnail',
    'practitioner',
    'patients',
    'practice',
    'reviews',
    'hitcount',
    # The Django sites framework is required
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter',
    #django REST Api
    #'rest_framework',
    #'rest_framework.authtoken',
    #django REST AUTH
    #'rest_auth'
)

#hitcount settings
SESSION_SAVE_EVERY_REQUEST = True

#Registration
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_OPEN = True
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_PAGE = BASE_URL + 'accounts/login'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    # This is required by allauth template tags
    'django.core.context_processors.request',
    # These are allauth specific context processors
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
    'docors.customProcessor.customProcessor',
)

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
LOGIN_REDIRECT_URL = '/'
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email', 'user_birthday'],
        'METHOD': 'oauth2',
        'VERIFIED_EMAIL': True
    }
}

ROOT_URLCONF = 'docors.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'docors.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'Rana_Gujjar',
        'USER': 'asadrana',
        'PASSWORD': 'asad0321',
        'HOST': 'localhost',
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Karachi'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#Static asset configuration
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # <-- docors/docors/...
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))   # <-- docors/...

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

GEOIP_PATH = os.path.join(BASE_DIR, "GeoIP/")

STATICFILES_DIRS = [ os.path.join(BASE_DIR, "project_static") ]
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

if DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, "venv/static/")
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    STATIC_ROOT = os.path.join(BASE_DIR, "venv/static/")
    ALLOWED_HOSTS = ['beta.doctorsinfo.pk']
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
