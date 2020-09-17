from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_lifecycle import LifecycleModelMixin

from .managers import MyUserManager


class User(LifecycleModelMixin, AbstractUser):
    email = models.EmailField(
        _("email address"),
        unique=True,
        help_text=_(
            "Required. Must be a valid email address. This is what you will use to log in."
        ),
        error_messages={"unique": _("A user with that email address already exists."),},
    )

    username = None

    USERNAME_FIELD = "email"

    # The docs claim this field is ONLY used in the creation of a super user.
    # See: https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#django.contrib.auth.models.CustomUser.REQUIRED_FIELDS
    REQUIRED_FIELDS = []

    objects = MyUserManager()
