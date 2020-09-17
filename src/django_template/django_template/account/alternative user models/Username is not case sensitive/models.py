from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_lifecycle import LifecycleModelMixin, hook, BEFORE_SAVE

from .managers import MyUserManager


class User(LifecycleModelMixin, AbstractUser):
    # This will keep track of the casing the user originally types.
    display_name = models.CharField(_("display name"), max_length=150, blank=True)

    # This is used to provide a case insensitive username.
    objects = MyUserManager()

    @hook(BEFORE_SAVE, when="username", has_changed=True)
    def lower_username(self):
        """
        If the username has changed, preserve the casing in self.display_name
        and then perform a lower() on the username field to aid in ensuring
        two usernames of different casing cannot be created.
        """
        self.display_name = self.username
        self.username = str.lower(self.username)

    def __str__(self):
        return f"{self.display_name}"
