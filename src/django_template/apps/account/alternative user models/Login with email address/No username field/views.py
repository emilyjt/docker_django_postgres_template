from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import MyUserCreationForm

User = get_user_model()


class RegisterView(CreateView):
    model = User
    form_class = MyUserCreationForm
    template_name = "account/register.html"

    def get_success_url(self):
        # Example messages implementation. You will need to add this to your html templates to be
        # able to view it. See the docs here: https://docs.djangoproject.com/en/3.0/ref/contrib/messages/
        messages.success(
            self.request,
            "Your account has been created! You can now log in with your shiny new account",
        )
        return reverse_lazy("account:login")

    def get(self, request, *args, **kwargs):
        # Do not allow a logged in user to register a new account.
        # Redirect them to wherever freshly logged in users go to.
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Do not allow a logged in user to register a new account.
        # Redirect them to wherever freshly logged in users go to.
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().post(request, *args, **kwargs)


class MyLoginView(LoginView):
    template_name = "account/login.html"