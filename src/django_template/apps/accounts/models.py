from django.contrib.auth.models import AbstractUser


# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
class User(AbstractUser):
    pass


""" <--- delete if necessary
'''
The code included here, is an example custom user model that will change the default
username based login to be an email based login. The new user model still requires
a username, but this functionality could be easily overridden.
'''

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as DjangoUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.db import models


# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project


class UserManager(DjangoUserManager):
    def _create_user(self, email, username, password, **extra_fields):
        '''
        Create and save a user with the given email, username, and password.
        '''
        if (not email) or email == "":
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        email = self.normalize_email(email)
        username = self.model.normalize_username(username)

        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, username, password, **extra_fields)


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    email = models.EmailField(
        _("email address"),
        unique=True,
        help_text=_("Required. Must be a valid email address."),
        error_messages={"unique": _("A user with that email address already exists."),},
    )

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={"unique": _("A user with that username already exists."),},
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

"""  # <--- delete if necessary
