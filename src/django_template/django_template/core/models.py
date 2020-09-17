from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides
    self updating `created` and `updated` fields.

    Example:

        # django_template/someapp/models.py

        from django_template.core.models import TimeStampedModel

        # Create your models here.
        class SomeModel(TimeStampedModel):
            name = models.CharField(max_length=32, unique=True, blank=True)

    The above model will inherit the `created` and `updated` fields.
    To view them on the admin panel, something like the following would be needed:

        # django_template/someapp/admin.py
        fieldsets = (
            (None, {"fields": ("name",)}),
            (_("Object timestamps"), {"fields": ("updated", "created"), "classes": ("collapse",)},),
        )
        readonly_fields = ("updated", "created")
    """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
