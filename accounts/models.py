from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)


class UserManager(BaseUserManager):
    def create_user(
            self, email, first_name, last_name, password=None, is_active=True, is_merchant=False, is_admin=False):
        if not email:
            raise ValueError("Users must have an email address")

        if not password:
            raise ValueError("Users must have a password")

        if not first_name and not last_name:
            raise ValueError("Users must provide both names")

        user_obj = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        user_obj.set_password(password)
        user_obj.active = is_active
        user_obj.merchant = is_merchant
        user_obj.admin = is_admin
        user_obj.save(using=self._db)

        return user_obj

    def create_merchant_user(self, email, first_name, last_name, password):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_merchant=True
        )

        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_admin=True
        )

        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    active = models.BooleanField(default=True)
    merchant = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.full_name:
            return self.first_name + " " + self.last_name
        return self.email

    def get_short_name(self):
        return self.first_name

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
