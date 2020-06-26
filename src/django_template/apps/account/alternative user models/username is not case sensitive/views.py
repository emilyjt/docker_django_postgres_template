from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import MyUserCreationForm


# Create your views here.
class RegisterView(CreateView):
    model = get_user_model()
    form_class = MyUserCreationForm
    template_name = "registration/register.html"

    def get_success_url(self):
        # Example messages implementation. You will need to add this to your html templates to be
        # able to view it. See the docs here: https://docs.djangoproject.com/en/3.0/ref/contrib/messages/
        messages.success(
            self.request,
            "Your account has been created! You can now log in with your shiny new account",
        )
        return reverse_lazy("account:login")

    def get(self, request, *args, **kwargs):
        # If the user is logged in, move them on, as we don't want users with an account registering again
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # If the user is logged in, move them on, as we don't want users with an account registering again
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().post(request, *args, **kwargs)
