"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
>>>>>>> a6120792a626c93a53c70e731eb58ce82265ed62
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()
