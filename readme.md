# Setup
Adjust the following settings:

database location (line 13)
  'NAME': '/path/to/intanware/intanwaredb',

admin media prefix (line 58)
  ADMIN_MEDIA_PREFIX = '/path/to/intanware/lib/'

static document root (line 52)
  STATIC_DOC_ROOT = '/path/to/intanware/lib/'

template directories (line 57)
  "/path/to/intanware/templates/"

# Local development server

to run locally simply go inside the intanware folder and run 
  
  python manage.py runserver

this will enable the local development server to run on http://127.0.0.1:8000

admin is accessible on http://127.0.0.1:8000/admin

standard username and password is admin

# Deployment on apache

This package is prepared for deployment on apache web server.

To host it you would require:
- Python (min 2.5)
- Django 1.2.4
- mod_wsgi

The /apache folder holds the wsgi setting for hosting intanware on apache web server running under ubuntu 8.10

edit the apache_django_wsgi.conf and dj_hello.wsgi accordingly to your server configuration

also dont forget to add the following line to your apache2.conf

  Include /var/www/intanware/apache/apache_django_wsgi.conf


ENJOY!

