from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class MyUserManager(UserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = "{}__iexact".format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})


class User(AbstractUser):
    # This will keep track of the casing the user originally types.
    display_name = models.CharField(_("display name"), max_length=150, blank=True)

    # This is used to provide a case insensitive username.
    objects = MyUserManager()

    # Instance variable to track if username is being updated, to preserve casing
    __original_username = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_username = self.username  # remember the current username

    def save(self, *args, **kwargs):
        # If the username has changed, preserve the casing in self.display_name
        # and then perform a lower() on the username field to aid in ensuring
        # two usernames of different casing cannot be created.
        if self.username != self.__original_username:
            self.display_name = self.username
            self.username = str.lower(self.username)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.display_name}"
