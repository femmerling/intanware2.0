#!/usr/local/bin/python 
import os, sys 
sys.path.append("/var/www") 
sys.path.append("/var/www/intanware/") 
os.environ["DJANGO_SETTINGS_MODULE"] = "settings" 
os.environ["PYTHON_EGG_CACHE"] = "/tmp" 
import django.core.handlers.wsgi 
application = django.core.handlers.wsgi.WSGIHandler() 

