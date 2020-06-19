from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as DjangoUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(DjangoUserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = "{}__iexact".format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})


class User(AbstractUser):
    display_name = models.CharField(_("display name"), max_length=150, blank=True)

    objects = UserManager()

    def save(self, *args, **kwargs):
        self.display_name = self.username
        self.username = str.lower(self.username)
        return super().save(*args, **kwargs)
