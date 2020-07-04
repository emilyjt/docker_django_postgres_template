from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# Refrence to the user model for cleaner code
User = get_user_model()


@admin.register(User)
class MyUserAdmin(UserAdmin):
    """
    Just a basic custom model admin, almost an exact copy of the Django standard
    but with `last_login` and `date_joined` as read-only.
    """

    list_display = ("username", "email", "first_name", "last_name", "is_staff")

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    readonly_fields = ("last_login", "date_joined")

    search_fields = ("username", "email")
