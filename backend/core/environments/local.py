from .base import *
from ..env import env

DEBUG =  env.bool("DEBUG", default=True)

ALLOWED_HOSTS = ['*']

# Configuracion de la Base de datos

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST':env('DATABASE_HOST_DEV'),
        'NAME': env('DATABASE_NAME_DEV'),
        'USER':env('DATABASE_USER_DEV'),
        'PASSWORD': env("DATABASE_PASSWORD_DEV")
    }
}


