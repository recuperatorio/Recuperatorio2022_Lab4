from .dev import*

DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR/ 'db_prod.sqlite3',
    }
 }
