"""
WSGI config for InterFacultad project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/

"""

import os

from InterFacultad.data import data
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'InterFacultad.'+data)

# application = get_wsgi_application()
from dj_static import Cling

application= Cling(get_wsgi_application())
