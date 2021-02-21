from .base import *
from .base import os

# -----------------------------------------------------------------------------
# General
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/ref/settings/#secret-key
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# https://docs.djangoproject.com/en/3.2/ref/settings/#allowed-hosts
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

# -----------------------------------------------------------------------------
# Caches
# -----------------------------------------------------------------------------
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ.get("REDIS_URL"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # Mimicing memcache behavior.
            # https://github.com/jazzband/django-redis#memcached-exceptions-behavior
            # "IGNORE_EXCEPTIONS": True,
        },
    }
}

# -----------------------------------------------------------------------------
# Security
# -----------------------------------------------------------------------------
## https://docs.djangoproject.com/en/3.2/ref/settings/#secure-proxy-ssl-header
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
## https://docs.djangoproject.com/en/3.2/ref/settings/#secure-ssl-redirect
# SECURE_SSL_REDIRECT = True
## https://docs.djangoproject.com/en/3.2/ref/settings/#session-cookie-secure
# SESSION_COOKIE_SECURE = True
## https://docs.djangoproject.com/en/3.2/ref/settings/#csrf-cookie-secure
# CSRF_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/3.2/topics/security/#ssl-https
## https://docs.djangoproject.com/en/3.2/ref/settings/#secure-hsts-seconds
## TODO: set this to 60 seconds first and then to 518400 once you prove 60 works
## SECURE_HSTS_SECONDS = 60
## https://docs.djangoproject.com/en/3.2/ref/settings/#secure-hsts-include-subdomains
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
## https://docs.djangoproject.com/en/3.2/ref/settings/#secure-hsts-preload
# SECURE_HSTS_PRELOAD = True
## https://docs.djangoproject.com/en/3.2/ref/middleware/#x-content-type-options-nosniff
# SECURE_CONTENT_TYPE_NOSNIFF = True

# -----------------------------------------------------------------------------
# Templates
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/ref/settings/#templates
TEMPLATES[-1]["OPTIONS"]["loaders"] = [  # type: ignore[index] # noqa F405
    (
        "django.template.loaders.cached.Loader",
        [
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ],
    )
]

# -----------------------------------------------------------------------------
# Email
# -----------------------------------------------------------------------------
# # https://docs.djangoproject.com/en/3.2/ref/settings/#default-from-email
# DEFAULT_FROM_EMAIL = env(
#     "DJANGO_DEFAULT_FROM_EMAIL", default="templates_django <noreply@example.com>"
# )
# # https://docs.djangoproject.com/en/3.2/ref/settings/#server-email
# SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)
# # https://docs.djangoproject.com/en/3.2/ref/settings/#email-subject-prefix
# EMAIL_SUBJECT_PREFIX = env(
#     "DJANGO_EMAIL_SUBJECT_PREFIX", default="[templates_django]"
# )

# -----------------------------------------------------------------------------
# Anymain
# -----------------------------------------------------------------------------
# # https://anymail.readthedocs.io/en/stable/installation/#installing-anymail
# INSTALLED_APPS += ["anymail"]  # noqa F405
# # https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
# # https://anymail.readthedocs.io/en/stable/installation/#anymail-settings-reference
# # https://anymail.readthedocs.io/en/stable/esps/mailgun/
# EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
# ANYMAIL = {
#     "MAILGUN_API_KEY": env("MAILGUN_API_KEY"),
#     "MAILGUN_SENDER_DOMAIN": env("MAILGUN_DOMAIN"),
#     "MAILGUN_API_URL": env("MAILGUN_API_URL", default="https://api.mailgun.net/v3"),
# }

# -----------------------------------------------------------------------------
# Logging
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
#     "formatters": {
#         "verbose": {
#             "format": "%(levelname)s %(asctime)s %(module)s "
#             "%(process)d %(thread)d %(message)s"
#         }
#     },
#     "handlers": {
#         "mail_admins": {
#             "level": "ERROR",
#             "filters": ["require_debug_false"],
#             "class": "django.utils.log.AdminEmailHandler",
#         },
#         "console": {
#             "level": "DEBUG",
#             "class": "logging.StreamHandler",
#             "formatter": "verbose",
#         },
#     },
#     "root": {"level": "INFO", "handlers": ["console"]},
#     "loggers": {
#         "django.request": {
#             "handlers": ["mail_admins"],
#             "level": "ERROR",
#             "propagate": True,
#         },
#         "django.security.DisallowedHost": {
#             "level": "ERROR",
#             "handlers": ["console", "mail_admins"],
#             "propagate": True,
#         },
#     },
# }
