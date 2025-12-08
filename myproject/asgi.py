"""
ASGI config for myproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
>>>>>>> a6120792a626c93a53c70e731eb58ce82265ed62
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_asgi_application()
