from django.views.generic.base import TemplateView

import random


# https://docs.djangoproject.com/en/3.0/ref/class-based-views/
class HomePageView(TemplateView):
    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["number"] = random.randrange(1, 100)
        return context


# Taken from https://docs.djangoproject.com/en/3.0/topics/class-based-views/mixins/#using-singleobjectmixin-with-view

# from django.http import HttpResponseForbidden, HttpResponseRedirect
# from django.urls import reverse
# from django.views import View
# from django.views.generic.detail import SingleObjectMixin
# from books.models import Author

# class RecordInterest(SingleObjectMixin, View):
#     """Records the current user's interest in an author."""
#     model = Author

#     def post(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return HttpResponseForbidden()

#         # Look up the author we're interested in.
#         self.object = self.get_object()
#         # Actually record interest somehow here!

#         return HttpResponseRedirect(reverse('author-detail', kwargs={'pk': self.object.pk}))
