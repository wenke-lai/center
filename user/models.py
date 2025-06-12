from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as AbstractUserManager
from django.db import models


class UserManager(AbstractUserManager):
    pass


class User(AbstractUser):
    clerk_id = models.CharField(
        max_length=255, unique=True, default=None, blank=True, null=True
    )

    objects = UserManager()
