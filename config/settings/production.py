from .base import *

SECRET_DEV_FILE = os.path.join(SECRETS_PATH, 'development.json')

secrets = json.loads(open(SECRET_DEV_FILE).read())

for key, value in secrets.items():
    setattr(sys.modules[__name__], key, value)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS += []


INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

WSGI_APPLICATION = 'config.wsgi.production.application'