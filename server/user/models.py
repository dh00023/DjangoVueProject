from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    AbstractUser,
    PermissionsMixin
)
from django.db import models
from django.utils import timezone
import uuid

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Email missing')
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            email=email,
            username=username,
            password=password
        )
        user.is_admin = True

        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=30, default="")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    date_joined = models.DateTimeField(default=timezone.now)
    
    objects = UserManager()

    # users are identified by email
    USERNAME_FIELD = 'email'
    # required fields to registe
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'users'

    def __str__(self):
        return "username: " + self.username

    @property
    def is_staff(self):
        return self.is_admin

    def has_module_perms(self, app_label):
        if self.is_active:
            return True

    def has_perm(self, perm, obj=None):
        if self.is_active and self.is_admin:
            return True

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username
