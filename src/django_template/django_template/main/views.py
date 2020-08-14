"""
# https://spookylukey.github.io/django-views-the-right-way/the-pattern.html
# spookylukey is a core @django developer, freelancer.
# https://github.com/spookylukey
#
# Below is his recommendation on views:

from django.template.response import TemplateResponse

def example_view(request, arg):
    return TemplateResponse(request, 'example.html', {})

"""

import random  # We need random to demonstrate passing values to a webpage

from django.template.response import TemplateResponse


def home(request):
    return TemplateResponse(
        request, "main/home.html", {"number": random.randrange(1, 100)}
    )
