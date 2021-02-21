from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import MyUserManager


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    email = models.EmailField(
        _("email address"),
        unique=True,
        help_text=_(
            "Required. Must be a valid email address. This is what you will use to log in."
        ),
        error_messages={
            "unique": _("A user with that email address already exists."),
        },
    )

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = MyUserManager()
