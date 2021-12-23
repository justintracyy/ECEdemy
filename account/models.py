import uuid

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import Group, AbstractUser, UserManager as OldUserManager
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class UserManager(OldUserManager):
    pass


class AccountUser(AbstractUser, models.Model):
    class Meta:
        verbose_name = 'Account User'
        verbose_name_plural = 'Accounts  User'

    objects = UserManager()
