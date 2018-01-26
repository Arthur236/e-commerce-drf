from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)


class UserManager(BaseUserManager):
    def create_user(
            self, username, email, password=None, is_active=True, is_merchant=False, is_admin=False):

        if not username:
            raise ValueError("Users must have a username")

        if not email:
            raise ValueError("Users must have an email address")

        if not password:
            raise ValueError("Users must have a password")

        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")

        user_obj = self.model(
            username=username,
            email=self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.active = is_active
        user_obj.merchant = is_merchant
        user_obj.admin = is_admin
        user_obj.save(using=self._db)

        return user_obj

    def create_merchant_user(self, username, email, password):
        user = self.create_user(
            username,
            email,
            password=password,
            is_merchant=True
        )

        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username,
            email,
            password=password,
            is_admin=True
        )

        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=120, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    merchant = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'

    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_merchant(self):
        return self.merchant

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.is_admin
