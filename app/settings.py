from .settingsbase import *
from .utils import getConfig

config = getConfig()
SECRET_KEY = config["system"]["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config["system"]["DEBUG"]

ALLOWED_HOSTS = config["system"]["ALLOWED_HOSTS"]
CSRF_TRUSTED_ORIGINS = config["system"]["CSRF_TRUSTED_ORIGINS"]
DATABASES = {
    'default': {
        'ENGINE': config["system"]["database"]["ENGINE"],
        'NAME': config["system"]["database"]["NAME"],
        'USER': config["system"]["database"]["USER"],
        'PASSWORD': config["system"]["database"]["PASSWORD"],
        'HOST': config["system"]["database"]["HOST"],
        'PORT': config["system"]["database"]["PORT"],
    }
}

STATIC_URL = config["system"]["static_url"]
