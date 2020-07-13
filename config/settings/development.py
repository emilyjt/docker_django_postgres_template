import os

from .base import *

"""
-------------------------------------------------------------------------------
General
-------------------------------------------------------------------------------
"""
DEBUG = True

SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY_DJANGO_TEMPLATE",
    b"yP\x90\xd4\xe8\xfb\x85k\x8c\x84r\xb5\x18\x8fV\xcc4sh\x90\xc6 <9",
)

ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]

INSTALLED_APPS += [
    "debug_toolbar",
]

"""
-------------------------------------------------------------------------------
Middleware
-------------------------------------------------------------------------------
"""
MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

"""
-------------------------------------------------------------------------------
django-debug-toolbar
-------------------------------------------------------------------------------
"""
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#configuring-internal-ips
INTERNAL_IPS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]
