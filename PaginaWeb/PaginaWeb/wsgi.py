"""
WSGI config for PaginaWeb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

import sys

# Añadir el directorio del proyecto a sys.path
sys.path.append('/opt/render/MyCineAvg_diego_guerrero/PaginaWeb')
sys.path.append('/opt/render/MyCineAvg_diego_guerrero/PaginaWeb/PaginaWeb')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PaginaWeb.settings')
application = get_wsgi_application()