from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

User = get_user_model()

# nullable shorthand
nullable = {"default": None, "null": True, "blank": True}


def get_default_deadline():
    """返回 30 天後的時間作為預設截止日期"""
    return timezone.now() + timedelta(days=30)


class Goal(models.Model):
    """目標模型"""

    class StateChoices(models.TextChoices):
        IN_PROGRESS = "in_progress", _("進行中")
        PENDING_VERIFICATION = "pending_verification", _("等待驗證")
        COMPLETED = "completed", _("完成")
        VERIFICATION_TIMEOUT = "verification_timeout", _("驗證超時")

    name = models.CharField(max_length=200, verbose_name=_("名稱"))
    description = models.TextField(verbose_name=_("描述"), **nullable)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("建立時間"))
    deadline = models.DateTimeField(
        default=get_default_deadline, verbose_name=_("截止日期")
    )
    state = models.CharField(
        max_length=20,
        choices=StateChoices.choices,
        default=StateChoices.IN_PROGRESS,
        verbose_name=_("狀態"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("使用者"),
        related_name="goals",
    )

    class Meta:
        verbose_name = _("目標")
        verbose_name_plural = _("目標")
        ordering = ["deadline"]

    def __str__(self):
        return self.name
