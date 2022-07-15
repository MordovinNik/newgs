from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '7cfj03te4*$wfasdg41h41-438fdg1fgsamo@&af+d0bfn1@zwkavb(jg=-n=p1!c@%@_$74'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [BASE_DIR / '../site/client/build/static']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
