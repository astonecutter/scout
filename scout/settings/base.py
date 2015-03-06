"""
Django settings for scout project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from djangae.settings_base import * #Set up some AppEngine specific stuff

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

from scout.boot import get_app_config
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_app_config().secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangosecure',
    'csp',
    'djangae.contrib.gauth',
    'djangae', # Djangae should be after Django core/contrib things
    'crispy_forms',

    'scout.markers',
    'scout.properties',
    'scout.sharing',
)

MIDDLEWARE_CLASSES = (
    'djangae.contrib.security.middleware.AppEngineSecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'scout.sharing.middleware.CustomAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
    'session_csrf.CsrfMiddleware',
    'djangosecure.middleware.SecurityMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "session_csrf.context_processor"
)

def check_session_csrf_enabled():
    if "session_csrf.CsrfMiddleware" not in MIDDLEWARE_CLASSES:
        return [ "SESSION_CSRF_DISABLED"]

    return []
check_session_csrf_enabled.messages = { "SESSION_CSRF_DISABLED" : "Please add 'session_csrf.CsrfMiddleware' to MIDDLEWARE_CLASSES" }

SECURE_CHECKS = [
    "djangosecure.check.sessions.check_session_cookie_secure",
    "djangosecure.check.sessions.check_session_cookie_httponly",
    "djangosecure.check.djangosecure.check_security_middleware",
    "djangosecure.check.djangosecure.check_sts",
    "djangosecure.check.djangosecure.check_frame_deny",
    "djangosecure.check.djangosecure.check_ssl_redirect",
    "scout.settings.base.check_session_csrf_enabled"
]

ROOT_URLCONF = 'scout.urls'

WSGI_APPLICATION = 'scout.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

CSP_DEFAULT_SRC = (
    "'self'",
    "https://ssl.gstatic.com",
    "https://maps.gstatic.com",
    "https://apis.google.com",
)

CSP_SCRIPT_SRC = (
    "'self'",
    "'unsafe-inline'",
    "'unsafe-eval'",
    "https://apis.google.com",
    "https://*.googleapis.com",
    "https://*.gstatic.com",
    "https://maxcdn.bootstrapcdn.com"
)

CSP_STYLE_SRC = (
    "'self'",
    "'unsafe-inline'",
    "https://fonts.googleapis.com",
    "https://maxcdn.bootstrapcdn.com"
)

CSP_FONT_SRC = (
    "'self'",
    "https://fonts.gstatic.com",
    "https://maxcdn.bootstrapcdn.com"
)

CSP_IMG_SRC = (
    "'self'",
    # FIFE domains
    # "https://lh3.googleusercontent.com",
    # "https://lh4.googleusercontent.com",
    # "https://lh5.googleusercontent.com",
    # "https://lh6.googleusercontent.com",
    # "https://lh3.ggpht.com",
    # "https://lh4.ggpht.com",
    # "https://lh5.ggpht.com",
    # "https://lh6.ggpht.com",
    "https://*.googleapis.com",
    "https://*.gstatic.com",
    "https://maps.google.com",
)

AUTH_USER_MODEL = 'djangae.GaeDatastoreUser'
AUTHENTICATION_BACKENDS = (
    'scout.sharing.backends.CustomAppEngineUserAPI',
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'