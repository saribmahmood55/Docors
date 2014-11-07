from django.conf import global_settings
import os

boolean = lambda value: bool(int(value))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zky%mapoo709@yv64h!ny#!7x8#&lh0o9nsfo++ny6+7gotp^r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = boolean(os.environ.get('DEBUG', 1))
TEMPLATE_DEBUG = DEBUG


ADMINS = (
    ('Asad Naeem', 'doctorsinfo.pk@gmail.com'),
)

#Sites
SITE_ID = 1

#Registration
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_OPEN = True
LOGIN_REDIRECT_URL = '/'

#GMAIL
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'doctorsinfo.pk@gmail.com'
EMAIL_HOST_PASSWORD = 'qtmtzmguforqkfkt'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
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
    'registration',
    'practitioner',
    'patients',
    'practice',
    'reviews'
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
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

#heroku
import dj_database_url
DATABASES = {}
DATABASES['default'] =  dj_database_url.config(default='postgres://ukmmuiwdvgoedx:rKUzM9TsSZ3VEiRywilVctUmvN@ec2-54-197-237-120.compute-1.amazonaws.com:5432/dc18vrdjn47bc0')
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

'''
import dj_database_url
DATABASES['default'] = dj_database_url.config()
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
'''

'''
import dj_database_url
DATABASES = {}
DATABASES['default'] =  dj_database_url.config(default='postgres://ukmmuiwdvgoedx:rKUzM9TsSZ3VEiRywilVctUmvN@ec2-54-197-237-120.compute-1.amazonaws.com:5432/dc18vrdjn47bc0')
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'geodjango',
        'USER': 'asadrana',
        'PASSWORD': 'asad0321',
        'HOST': 'localhost',
    }
}
'''
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

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

# Static asset configuration
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # <-- docors/docors/...
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))   # <-- docors/...   project root

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # <-- docors/docors/...

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
