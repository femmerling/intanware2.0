# Django settings for intanware project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ( 'Intanware Admin', 'intanware@emfeld.com')

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': '/root/intanware/intanwaredb',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = ''

MEDIA_URL = ''

ADMIN_MEDIA_PREFIX = '/root/intanware/lib/'

SECRET_KEY = 'l7+zpxyau1w@9edw3ua)&3eq%@z%kzz4xb%a%on@*^u&_p04bb'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

STATIC_DOC_ROOT = '/root/intanware/lib/'

ROOT_URLCONF = 'intanware.urls'

TEMPLATE_DIRS = (
    "/root/intanware/templates/"
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'page',
    'django.contrib.admin',
)
