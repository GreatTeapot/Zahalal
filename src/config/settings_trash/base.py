from pathlib import Path
import os
import mimetypes
import environ
from pathlib import Path

from dotenv import load_dotenv
import mimetypes

root = environ.Path(__file__)
env = environ.Env()
environ.Env.read_env(env.str(root(), default='.env'))

load_dotenv()
mimetypes.add_type("text/javascript", ".js", True)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str(var='SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool(var='DEBUG', default=False)
ALLOWED_HOSTS = env.str(var='ALLOWED_HOSTS', default='').split(' ')

# region --------------------------- CORS HEADERS -----------------------------------

CORS_ALLOW_ALL_ORIGINS = True  # Разрешаем все источники

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    
]

CORS_ALLOW_CREDENTIALS = True  # Разрешаем отправку куки и учетных данных

CORS_ALLOWED_METHODS = [
    "GET", "POST", "PUT", "DELETE", "PATCH"
]  # Разрешенные HTTP методы

CORS_ALLOWED_HEADERS = [
    "Authorization",  # Разрешаем заголовок для авторизации
    "Content-Type",  # Разрешаем заголовок Content-Type
    "X-Requested-With",  # Для поддержки AJAX-запросов
    "Accept",  # Разрешаем заголовок Accept
    "Origin",  # Заголовок Origin, который браузеры посылают при кросс-доменных запросах
    "X-CSRFToken",  # Если используется защита CSRF
    "Access-Control-Allow-Origin", # Разрешаем заголовок Access-Control-Allow-Origin
]
CSRF_TRUSTED_ORIGINS = [
    

]

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Application definition

BASE_DIR = Path(__file__).resolve().parent.parent.parent

INSTALLED_APPS = [
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # else
    'rest_framework',
    'drf_spectacular',
    'corsheaders',



    # apps
    'apps.cards',
    'apps.categories',
    'apps.reviews',
    'apps.users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str(var='PG_DATABASE', default='postgres'),
        'USER': env.str(var='PG_USER', default='postgres'),
        'PASSWORD': env.str(var='PG_PASSWORD', default='postgres'),
        'HOST': env.str(var='PG_HOST', default='localhost'),
        'PORT': env.int(var='PG_PORT', default=5432),
    },
    'extra': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

LOGIN_REDIRECT_URL = '/admin/'

SPECTACULAR_SETTINGS = {
    'TITLE': 'Zahalal API',
    'DESCRIPTION': 'API для проекта Zahalal',
    'VERSION': '1.0.0',
}


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join('static/')

STATIC_ROOT = '/usr/src/app/static/'


MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join('media/')
# MEDIA_TEST_ROOT = os.path.join(BASE_DIR, 'media/test/')

MEDIA_ROOT = '/usr/src/app/media/' 

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'