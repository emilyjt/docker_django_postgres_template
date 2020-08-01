import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
APPS_DIR = os.path.join(BASE_DIR, "django_template")

# -----------------------------------------------------------------------------
# General
# -----------------------------------------------------------------------------

# Default is False, but this variable should be passed in from Docker
# The value it receives is in .envs/<environment>/.django
DEBUG = os.getenv("DJANGO_DEBUG", False)

# This variable should be passed in from Docker
# The value it receives is in .envs/<environment>/.django
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# This variable should be passed in from Docker
# The value it receives is in .envs/<environment>/.django
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS",).split(" ")

# https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-SESSION_COOKIE_AGE
SESSION_COOKIE_AGE = 1209600

# https://docs.djangoproject.com/en/3.0/ref/settings/#site-id
SITE_ID = 1

# https://docs.djangoproject.com/en/3.0/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

# https://docs.djangoproject.com/en/3.0/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"

# -----------------------------------------------------------------------------
# Applications
# -----------------------------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Start of your entries
    "django_template.account",
    "django_template.main",
]

# -----------------------------------------------------------------------------
# Email
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Database
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("POSTGRES_ENGINE"),
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    }
}

# -----------------------------------------------------------------------------
# Authentication
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-user-model
AUTH_USER_MODEL = "account.User"
# https://docs.djangoproject.com/en/3.0/ref/settings/#login-url
LOGIN_URL = "account:login"
# https://docs.djangoproject.com/en/3.0/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "main:home"
# https://docs.djangoproject.com/en/3.0/ref/settings/#logout-redirect-url
LOGOUT_REDIRECT_URL = "main:home"

# -----------------------------------------------------------------------------
# Authentication
# -----------------------------------------------------------------------------

# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {"min_length": 8,},
    },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

# -----------------------------------------------------------------------------
# Middleware
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.0/ref/settings/#middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    # "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# -----------------------------------------------------------------------------
# Static
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.0/ref/settings/#static-root
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# https://docs.djangoproject.com/en/3.0/ref/settings/#static-url
STATIC_URL = "/static/"

# https://docs.djangoproject.com/en/3.0/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [
    os.path.join(APPS_DIR, "static"),
]

# In case someone attempts to use media files with pillow.
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

# -----------------------------------------------------------------------------
# Templates
# -----------------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(APPS_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# -----------------------------------------------------------------------------
# Admin
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.0/ref/settings/#admins
ADMINS = [("Emily", "12156026+emilyjt@users.noreply.github.com")]

# https://docs.djangoproject.com/en/3.0/ref/settings/#managers
MANAGERS = ADMINS

# -----------------------------------------------------------------------------
# Internationalization
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.0/topics/i18n/

# https://docs.djangoproject.com/en/3.0/ref/settings/#language-code
LANGUAGE_CODE = "en-gb"

# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = "GB"

# https://docs.djangoproject.com/en/3.0/ref/settings/#use-i18n
USE_I18N = True

# https://docs.djangoproject.com/en/3.0/ref/settings/#use-l10n
USE_L10N = True

# https://docs.djangoproject.com/en/3.0/ref/settings/#use-tz
USE_TZ = True

# https://docs.djangoproject.com/en/3.0/ref/settings/#locale-paths
LOCALE_PATHS = (os.path.join(APPS_DIR, "locale"),)
