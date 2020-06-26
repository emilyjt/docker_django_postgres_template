from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.utils.translation import gettext_lazy as _


class MyUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_texts(),
    )

    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
    }

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            get_user_model().objects.exclude(pk=self.instance.pk).get(
                username=str.lower(username)
            )

        except get_user_model().DoesNotExist:
            return username

        raise forms.ValidationError(
            get_user_model().username.field.error_messages.get("unique"),
            code="username_unique",
        )

    class Meta:
        model = get_user_model()
        fields = ("username",)
        field_classes = {"username": UsernameField}
