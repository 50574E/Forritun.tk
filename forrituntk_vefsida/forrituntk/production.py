from .base import *

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DEBUG = False
INSTALLED_APPS += (
    # production-only apps
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '',
    }
}

DISCOURSE_BASE_URL = 'http://discourse.forritun.tk'
DISCOURSE_SSO_SECRET = os.environ['DISCOURSE_SSO_SECRET']