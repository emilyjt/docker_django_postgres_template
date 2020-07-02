from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as UserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import MyUserCreationForm

User = get_user_model()


# @admin.register(User)  # <-- this line will need to uncommented
class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm

    list_display = ("username", "email", "first_name", "last_name", "is_staff")

    fieldsets = (
        (None, {"fields": ("username", "display_name", "password")}),
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
                # "classes": ("collapse",),  # optionally uncomment and view a user account in admin
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    readonly_fields = ("display_name", "last_login", "date_joined")

    search_fields = ("username", "email")
