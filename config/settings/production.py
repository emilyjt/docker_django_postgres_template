import os

from .base import *

"""
-------------------------------------------------------------------------------
General
-------------------------------------------------------------------------------
"""
DEBUG = False

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY_DJANGO_TEMPLATE")

ALLOWED_HOSTS = [
    # "somewebsite.co.uk",
    # "someheroku.herokuapp.com",
]
