from django.views.generic.base import TemplateView

import random


# https://docs.djangoproject.com/en/3.0/ref/class-based-views/base/
class HomePageView(TemplateView):
    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["number"] = random.randrange(1, 100)
        return context
