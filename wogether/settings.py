"""
Django settings for wogether project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

from wogether.app_settings.allauth import *  # @UnusedWildImport
#from wogether.app_settings.grappelli import *  # @UnusedWildImport
from wogether.app_settings.guardian import *  # @UnusedWildImport
from wogether.app_settings.rest import *  # @UnusedWildImport
from wogether.app_settings.restauth import *  # @UnusedWildImport

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+wt@m4xb5e(h4epc#6mo#m-e_^d0b_veaix+h$2hth2(r20grr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

SITE_ID = 1

#########################################
# EMAIL CONFIGURATION
#########################################
EMAIL_HOST = '192.168.0.250'
#  EMAIL_HOST_PASSWORD = ''
#  EMAIL_HOST_USER = ''
#  EMAIL_PORT = 25
EMAIL_SUBJECT_PREFIX = '[Wogether]'
DEFAULT_FROM_EMAIL = 'no-reply@wogether.com'



# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'matthieu.oscuro@gmail.com'
# EMAIL_HOST_PASSWORD = 'marionne44'
# EMAIL_SUBJECT_PREFIX = '[Wogether]'
# #DEFAULT_FROM_EMAIL = 'no-reply@wogether.com'
# 
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# 
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


ROOT_URLCONF = 'wogether.urls'

EXTERNAL_URLCONFS = (
    (os.environ.get('FRONTEND_URL', 'http://127.0.0.1:8000'), 'wogether.urls_external'),
)

# Login redirection rule
#LOGIN_REDIRECT_URL = "/api/v1/"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # The Django sites framework is required for allauth app
    'django.contrib.sites',

    # Contribution apps
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_auth.registration',
    'guardian',
    'treebeard',
    
    # Wogether apps
    'user_account',
    'workout',
    'round',
    'exercise',
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

ROOT_URLCONF = 'wogether.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'wogether.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

    'guardian.backends.ObjectPermissionBackend',
)

AUTH_USER_MODEL = 'user_account.User'

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
