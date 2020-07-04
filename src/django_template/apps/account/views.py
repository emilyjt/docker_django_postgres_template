from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

User = get_user_model()


class MyRegisterView(CreateView):
    """
    This view allows a user to register an account.
    https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-editing/#createview
    """

    model = User
    form_class = UserCreationForm
    template_name = "account/register.html"

    def get_success_url(self):
        """
        Example messages implementation. You will need to add this to your html templates to be
        able to view it. See the docs here: https://docs.djangoproject.com/en/3.0/ref/contrib/messages/
        """
        messages.success(
            self.request,
            "Your account has been created! You can now log in with your shiny new account",
        )
        return reverse_lazy("account:login")

    def get(self, request, *args, **kwargs):
        """
        Do not allow a logged in user to register a new account.
        Redirect them to wherever freshly logged in users go to.
        """
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Do not allow a logged in user to register a new account.
        Redirect them to wherever freshly logged in users go to.
        """
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().post(request, *args, **kwargs)


class MyLoginView(LoginView):
    """
    Simple override to change the template location from `registration/login.html`
    to `account/login.html`.
    This is for clarity. The app is named account, and so the templates should also
    be located in account.
    """

    template_name = "account/login.html"


class MyLogoutView(LogoutView):
    """
    Simple override to change the template location from `registration/logged_out.html`
    to `account/logged_out.html`.
    This is for clarity. The app is named account, and so the templates should also
    be located in account.
    """

    template_name = "account/logged_out.html"


class MyPasswordChangeView(PasswordChangeView):
    """
    Simple override to change the template location from `registration/password_change_form.html`
    to `account/password_change_form.html`, and to change the success_url to
    the namespaced variant.
    This is for clarity. The app is named account, and so the templates should also
    be located in account.
    """

    template_name = "account/password_change_form.html"
    success_url = reverse_lazy("account:password_change_done")


class MyPasswordChangeDoneView(PasswordChangeDoneView):
    """
    Simple override to change the template location from `registration/password_change_done.html`
    to `account/password_change_done.html`.
    This is for clarity. The app is named account, and so the templates should also
    be located in account.
    """

    template_name = "account/password_change_done.html"


class MyPasswordResetView(PasswordResetView):
    """
    Simple override to change the template location from `registration/password_reset_email.html`
    to `account/password_reset_email/body.html`, and to change the success_url to
    the namespaced variant.
    This is for clarity. The app is named account, and so the templates should also
    be located in account.
    """

    subject_template_name = "account/password_reset_email/subject.txt"
    email_template_name = "account/password_reset_email/body.html"
    html_email_template_name = None
    success_url = reverse_lazy("account:password_reset_done")
    template_name = "account/password_reset_form.html"


class MyPasswordResetDoneView(PasswordResetDoneView):
    """
    Simple override to change the template location from `registration/password_reset_done.html`
    to `account/password_reset_done.html`.
    This is for clarity. The app is named account, and so the templates should also
    be located in account.
    """

    template_name = "account/password_reset_done.html"


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    """
    Simple override to change the template location from `registration/password_reset_confirm.html`
    to `account/password_reset_confirm.html`, and to change the success_url to
    the namespaced variant.
    This is for clarity. The app is named account, and so the templates should also
    be located in account.
    """

    success_url = reverse_lazy("account:password_reset_complete")
    template_name = "account/password_reset_confirm.html"


class MyPasswordResetCompleteView(PasswordResetCompleteView):
    """
    Simple override to change the template location from `registration/password_reset_complete.html`
    to `account/password_reset_complete.html`.
    This is for clarity. The app is named account, and so the templates should also
    be located in account.
    """

    template_name = "account/password_reset_complete.html"
