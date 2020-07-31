from .base import *

# -----------------------------------------------------------------------------
# General
# -----------------------------------------------------------------------------
INSTALLED_APPS += [
    "debug_toolbar",
]

# -----------------------------------------------------------------------------
# Middleware
# -----------------------------------------------------------------------------
MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# -----------------------------------------------------------------------------
# django-debug-toolbar
# -----------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#configuring-internal-ips
INTERNAL_IPS = type(str("c"), (), {"__contains__": lambda *a: True})()
