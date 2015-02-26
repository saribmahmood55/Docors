from django.conf import global_settings
import os

boolean = lambda value: bool(int(value))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zky%mapoo709@yv64h!ny#!7x8#&lh0o9nsfo++ny6+7gotp^r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = boolean(os.environ.get('DEBUG', 0))
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Asad Naeem', 'anrana744@gmail.com'),
)
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

#Sites
SITE_ID = 1

#Registration
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_OPEN = True
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

#GMAIL
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'doctorsinfo.pk@gmail.com'
EMAIL_HOST_PASSWORD = 'qtmtzmguforqkfkt'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

#haystack
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}

#Raven
RAVEN_CONFIG = {
    'dsn': 'http://c7fc802b8e3d4fbeac0fe47e9f9d0569:3a6d3bac8f8d4136945877a2b7c3ebe1@sentry.localhost/2',
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
    'raven.contrib.django.raven_compat',
    'haystack',
    'registration',
    'sorl.thumbnail',
    'practitioner',
    'patients',
    'practice',
    'reviews',
)

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
    'django.core.context_processors.static',
)

ROOT_URLCONF = 'docors.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'docors.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'geodjango',
        'USER': 'asadrana',
        'PASSWORD': 'asad0321',
        'HOST': 'localhost',
    }
}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
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

# Allow all host headers
ALLOWED_HOSTS = ['*']

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

STATICFILES_DIRS = [
	os.path.join(BASE_DIR, "static")
]

if DEBUG:
    STATIC_ROOT = '/home/asad/docors/static/'
    MEDIA_ROOT = '/home/asad/docors/media/'
    
else:
    STATIC_ROOT = '/home/asad/docors/static/'
    MEDIA_ROOT = '/home/asad/docors/media/'