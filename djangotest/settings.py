"""
Django settings for djangotest project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd3m87izrh7(lco-q!l94a03*(cjm13e4em%keiv8l@(8y+svmh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	'rest_framework',
	'rest_framework.authtoken',
	'rest_auth',

	'frontend',
	'polls'
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

REST_FRAMEWORK = {
	# Use hyperlinked styles by default.
	# Only used if the `serializer_class` attribute is not set on a view.
	'DEFAULT_MODEL_SERIALIZER_CLASS':
		'rest_framework.serializers.HyperlinkedModelSerializer',

	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework.authentication.SessionAuthentication',
	),

	# Use Django's standard `django.contrib.auth` permissions,
	# or allow read-only access for unauthenticated users.
	'DEFAULT_PERMISSION_CLASSES': [
		'rest_framework.permissions.DjangoModelPermissions',
		#'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
	],

	'PAGINATE_BY_PARAM': 'limit',
	'ORDERING_PARAM': 'sort',

	'PAGINATE_BY': 10,
	'MAX_PAGINATE_BY': 100,

	'DEFAULT_FILTER_BACKENDS': [
		'rest_framework.filters.DjangoFilterBackend',
		'rest_framework.filters.OrderingFilter',
	],
}

LOGIN_REDIRECT_URL = '/api/'

ROOT_URLCONF = 'djangotest.urls'

WSGI_APPLICATION = 'djangotest.wsgi.application'


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
