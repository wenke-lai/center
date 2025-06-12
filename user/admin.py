from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
        "clerk_id",
    )

    fieldsets = (
        ("Personal info", {"fields": ("first_name", "last_name", "email", "clerk_id")}),
        (
            "Permissions",
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
        ("Authentication", {"fields": ("username", "password")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
