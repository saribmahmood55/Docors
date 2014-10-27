#from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
from django.conf import global_settings
import os
import dj_database_url

boolean = lambda value: bool(int(value))
local_path = lambda path: os.path.join(os.path.dirname(__file__), path)

#DATABASE_URL = "postgres://jimfzyyxmmgphs:igHjaN9x_SbjCzgsEs21yfVrsz@ec2-54-204-37-92.compute-1.amazonaws.com:5432/dd9m18h1llbkph"
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zky%mapoo709@yv64h!ny#!7x8#&lh0o9nsfo++ny6+7gotp^r'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = boolean(os.environ.get('DEBUG', 0))
TEMPLATE_DEBUG = DEBUG

# List of callables that know how to import templates from various sources.
if not DEBUG:
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )
else:
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

'''
if DEBUG: 
   STATIC_ROOT = os.path.join(BASE_DIR, '/static')
else:
   STATIC_ROOT = os.path.join(BASE_DIR, 'static')
'''

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
    'registration',
    'practitioner',
    'patients',
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

ROOT_URLCONF = '{{ project_name }}.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

TEMPLATE_DIRS = (
    local_path('templates/')
)


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'doctors_',
        'USER': 'asadrana',
        'PASSWORD': 'asad0321',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Karachi'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


# Parse database configuration from $DATABASE_URL
#DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}
DATABASES['default'] =  dj_database_url.config()

#DATABASES = {'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))}


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

'''
TEMPLATE_DIRS = (
    os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")), "templates"),
)
'''