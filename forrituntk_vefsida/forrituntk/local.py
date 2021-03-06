from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ee%7xdly+yxt0_=8t8s@mo%l)qsd2yzrbp@lj*fzwnyl2g97)z'

DEBUG = True
TEMPLATE_DEBUG = True

INSTALLED_APPS += (
    'debug_toolbar',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'forrituntk',
        'USER': 'forrituntk',
        'PASSWORD': 'forrituntk',
        'HOST': 'localhost',
        'PORT': '',
    }
}

DISCOURSE_BASE_URL = 'http://discourse.forritun.tk'
DISCOURSE_SSO_SECRET = os.getenv('DISCOURSE_SSO_SECRET', 'forrituntk')