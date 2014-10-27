#from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
from django.conf import global_settings
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zky%mapoo709@yv64h!ny#!7x8#&lh0o9nsfo++ny6+7gotp^r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

#
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

SITE_ID = 1

#Registration
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_OPEN = True

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

WSGI_APPLICATION = 'docors.wsgi.application'


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

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'



'''
STATIC_URL = '/static/'
TEMPLATE_DIRS = (
    os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")), "templates"),
)
STATICFILES_DIRS = (
    os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")), "project_static/"),
)
'''