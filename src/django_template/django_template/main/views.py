# We need random to demonstrate passing values to a webpage
import random

from django.template.response import TemplateResponse


def home(request, arg=None):
    return TemplateResponse(
        request, "main/home.html", {"number": random.randrange(1, 100)}
    )
