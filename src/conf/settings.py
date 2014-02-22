#coding:utf-8
import os
import json
from ConfigParser import RawConfigParser

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

config = RawConfigParser()
config.read(os.path.join(BASE_DIR, 'settings.ini'))

########## Версия сайта #####
CONF = 'kazan_prod'
# Доступные варианты:
#   kazan_prod
#   moscow_dev
#############################

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zlxl$x&65voq5+%d&8wo^@_hf_i&fre!%xm&9#zq9e)jo+e9b#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.get(CONF, 'DEBUG')
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.webdesign',

    'south',
    'pages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'conf.urls'

WSGI_APPLICATION = 'conf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'collected_static'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# weather
WEATHER_CITY = config.get(CONF, 'WEATHER_CITY')
WEATHER_CITY_TRANS = config.get(CONF, 'WEATHER_CITY_TRANS')
WEATHER_CITY_COORDINATES = json.loads(config.get(CONF, 'WEATHER_CITY_COORDINATES'))
WEATHER_CITY_TIMEOFFSET = config.getint(CONF, 'WEATHER_CITY_TIMEOFFSET')
WEATHER_API_URL = 'http://api.worldweatheronline.com/free/v1/weather.ashx'
WEATHER_API_KEY = '7wv697hms48fkth4b4r7hwtg'

CACHES = {
    "default": {
        "BACKEND": "redis_cache.cache.RedisCache",
        "LOCATION": "127.0.0.1:6379:1",
        "OPTIONS": {
            "CLIENT_CLASS": "redis_cache.client.DefaultClient",
        }
    }
}
# for drop management
ALL_CACHE_KEY = [
    'weather_api',
    'weather_sun'
]
