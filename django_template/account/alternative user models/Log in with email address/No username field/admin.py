from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# Refrence to the user model for cleaner code
User = get_user_model()


# @admin.register(User)  # <-- this line will need to uncommented
class MyUserAdmin(UserAdmin):
    list_display = ("email", "first_name", "last_name", "is_staff")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
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
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2"),},),
    )

    readonly_fields = ("last_login", "date_joined")
    search_fields = ("email",)
    ordering = ("email",)
