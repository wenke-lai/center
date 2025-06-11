from django.contrib import admin

from .models import Goal


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "state", "deadline", "created_at")
    list_filter = ("state", "created_at", "deadline")
    search_fields = ("name", "description")
    readonly_fields = ("created_at",)
    date_hierarchy = "deadline"

    fieldsets = (
        (None, {"fields": ("name", "description", "user", "state")}),
        ("時間設定", {"fields": ("deadline", "created_at")}),
    )
