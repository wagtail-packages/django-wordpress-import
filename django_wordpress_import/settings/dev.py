from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

LANGUAGE_CODE = "en-gb"

TIME_ZONE = "Europe/London"

USE_I18N = True

USE_TZ = False  # to silence waring for now

try:
    from .local import *
except ImportError:
    pass
