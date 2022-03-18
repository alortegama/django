# SECURITY WARNING: don't run with debug turned on in production!
from .base import *
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1','localhost']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "django",
        'USER': "django",
        'PASSWORD': "secret",
        'HOST': "django-postgre",
        'PORT': '5432',
    }
}
