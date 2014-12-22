from .base import *

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DEBUG = False
INSTALLED_APPS += (
    # production-only apps
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'forrituntk',
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '',
    }
}