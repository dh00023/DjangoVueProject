from .base import *

SECRET_DEV_FILE = os.path.join(SECRETS_PATH, 'development.json')

secrets = json.loads(open(SECRET_DEV_FILE).read())

for key, value in secrets.items():
    setattr(sys.modules[__name__], key, value)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS += [ 'local-display.cjmall.com', '127.0.0.1']

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions'
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

WSGI_APPLICATION = 'config.wsgi.development.application'
WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': DEBUG,
        'BUNDLE_DIR_NAME': '/bundles/',  # must end with slash
        'STATS_FILE': os.path.join(ROOT_DIR, 'webpack-stats.json'),
    }
}

# MEDIA_URL = '/media/' # media 파일에 대한 url prifix
# MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads') # 업로드된 파일을 저장할 디렉토리 경
# INTERNAL_IPS = ('127.0.0.1',)