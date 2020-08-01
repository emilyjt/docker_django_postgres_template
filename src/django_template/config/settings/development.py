from .base import *

# -----------------------------------------------------------------------------
# Applications
# -----------------------------------------------------------------------------
INSTALLED_APPS += [
    "debug_toolbar",
]

# -----------------------------------------------------------------------------
# Email
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.0/topics/email/#console-backend
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

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
