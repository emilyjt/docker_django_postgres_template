from .base import *
from .base import os

# -----------------------------------------------------------------------------
# General
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/ref/settings/#debug
DEBUG = True

# https://docs.djangoproject.com/en/3.2/ref/settings/#secret-key
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY", "=idnuuk58qay@29+duog_s398(3j&7a^28ybh9p-i@s5q$*j-@"
)

# https://docs.djangoproject.com/en/3.2/ref/settings/#allowed-hosts
ALLOWED_HOSTS = "localhost 127.0.0.1 [::1]".split(" ")

# -----------------------------------------------------------------------------
# Caches
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# -----------------------------------------------------------------------------
# Email
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/topics/email/#console-backend
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# -----------------------------------------------------------------------------
# Applications
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

# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}
