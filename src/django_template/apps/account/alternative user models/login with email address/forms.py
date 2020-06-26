from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField


class MyUserCreationForm(UserCreationForm):
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
        fields = ("email", "username")
        field_classes = {"email": forms.EmailField, "username": UsernameField}
