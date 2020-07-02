from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)
        field_classes = {"email": forms.EmailField}
