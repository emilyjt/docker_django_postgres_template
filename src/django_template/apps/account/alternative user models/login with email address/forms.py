from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

User = get_user_model()


class MyUserCreationForm(UserCreationForm):
    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.exclude(pk=self.instance.pk).get(username=str.lower(username))

        except User.DoesNotExist:
            return username

        raise forms.ValidationError(
            User.username.field.error_messages.get("unique"), code="username_unique",
        )

    class Meta:
        model = User
        fields = ("email", "username")
        field_classes = {"email": forms.EmailField, "username": UsernameField}
