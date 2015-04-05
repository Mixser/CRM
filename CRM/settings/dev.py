from .base import *

DEV = True
STAGING = False
PROD = False
ENV = 'DEV'

DEBUG = TEMPLATE_DEBUG = True
CURRENT_HOST = "127.0.0.1:8000"
BASE_URL = "http://" + CURRENT_HOST


ADMINS = (
    ('Mike', 'mike@razortheory.com'),
)

WEBSITE_MANAGERS = ADMINS
MANAGERS = ADMINS


CELERY_ALWAYS_EAGER = True
MEDIA_URL = BASE_URL + '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_FROM_EMAIL = 'noreply@mike.com'
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
