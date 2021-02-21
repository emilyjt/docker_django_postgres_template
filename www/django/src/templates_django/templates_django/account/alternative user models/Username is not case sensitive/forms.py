from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

# Refrence to the user model for cleaner code
User = get_user_model()


class MyUserCreationForm(UserCreationForm):
    def clean_username(self):
        """
        Checks if the username exists in the database

        All usernames are stored in the database in lower case, and so
        the username must be lower()'d before it is checked.

        :raises forms.ValidationError: this means the username already exists
        :return: the username, if it doesn't exist in the database - it will not be lower()'d
                 this is to be done in the save() method of the model.
        """
        username = self.cleaned_data["username"]
        try:
            User.objects.exclude(pk=self.instance.pk).get(username=str.lower(username))

        except User.DoesNotExist:
            return username

        raise forms.ValidationError(
            User.username.field.error_messages.get("unique"),
            code="username_unique",
        )

    class Meta:
        model = get_user_model()
        fields = ("username",)
        field_classes = {"username": UsernameField}
