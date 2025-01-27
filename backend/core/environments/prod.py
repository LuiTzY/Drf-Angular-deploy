from .base import *
from ..env import env


DEBUG =  env.bool("DEBUG",default=False)

#Configuracion de los hosts permitidos 
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

# Configuracion de la Base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST':env('DATABASE_HOST_PROD'),
        'NAME': env('DATABASE_NAME_PROD'),
        'USER':env('DATABASE_USER_PROD'),
        'PASSWORD': env("DATABASE_USER_PASSWORD_PROD")
    }
}

