from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import ugettext as _
import os


class AccountManager(BaseUserManager):

   def create_user(self,email, username,first_name,last_name,
                   password=None):
      """
      creates, validates and saves a new user
      :param email:
      :param username:
      :param password:
      :param extra_fields:
      :return:
      """
      if not email:
         raise ValueError("User must have an email")
      email       = self.normalize_email(email)
      user        = self.model(email=email,username=username,
                               first_name=first_name, last_name=last_name,
                               )
      user.set_password(password)
      user.save(using=self._db)
      return user

   def create_superuser(self, username, email, first_name, last_name,
                        password=None):
      user                 = self.create_user(username,email,first_name,last_name,
                                              password=password, )


      user.is_active       = True
      user.is_superuser    = True
      user.is_staff        = True

      user.set_password(password)
      user.save(using=self._db)
      return user


class AccountUser(AbstractBaseUser):

   """
   Custom User model that supports using email instead of username -- /
   Supported by PermissionsMixins
   """
   email            = models.EmailField(max_length=256, unique=True)
   username         = models.CharField(max_length=256, unique=True)
   first_name       = models.CharField(max_length=256)
   last_name        = models.CharField(max_length=256)
   is_active        = models.BooleanField(default=True)
   is_staff         = models.BooleanField(default=False)
   is_admin         = models.BooleanField(default=False)

   objects = AccountManager()

   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = ['username','first_name', 'last_name']

   def __str__(self):
      return self.email



   def has_perm(self, perm, obj=None):
      """
      Does the user have a specific permission?
      :param perm:
      :param obj:
      :return:
      """
      return True


   def has_module_perms(self, app_label):
      """
      Does the user have the permission to view the 'app_label'
      :param app_label:
      :return:
      """
      return True


   @property
   def is_staff(self):
      """
      Is the user a member of staff
      :return:
      """
      return self.is_admin

   @property
   def is_superuser(self):
      return self.is_admin
