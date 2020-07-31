from django.views.generic.base import TemplateView

# We need random to demonstrate passing values to a webpage
import random


# https://docs.djangoproject.com/en/3.0/ref/class-based-views/
class HomePageView(TemplateView):
    """This view will be our index located at "/"

    The template is located at src/django_template/apps/main/templates/main/home.html
    The important part is 'main/home.html'
    See here: https://docs.djangoproject.com/en/3.0/ref/settings/#templates
    for the important line: 'Here’s a setup that tells the Django template engine to
    load templates from the templates subdirectory inside each installed application'
    This mode is enabled in the settings.
    """

    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        """This function builds the data that will be passed to the template

        https://docs.djangoproject.com/en/3.0/ref/templates/api/#rendering-a-context

        For this example, all that is happening is a random number between 1 and 100
        is being generated.
        """
        context = super().get_context_data(**kwargs)
        context["number"] = random.randrange(1, 100)
        return context
