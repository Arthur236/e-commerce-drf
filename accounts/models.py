"""
Model definitions
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)


class UserManager(BaseUserManager):
    """
    Create our own custom user manager
    """
    def create_user(self, username, email, password=None):
        """
        Override the create user method
        """
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
        user_obj.save(using=self._db)

        return user_obj

    def create_superuser(self, username, email, password):
        """
        Override create superuser method
        """
        user = self.create_user(
            username,
            email,
            password=password
        )
        user.admin = True
        user.save(using=self._db)

        return user

    def create_merchant(self, username, email, password):
        """
        Create a merchant
        """
        user = self.create_user(
            username,
            email,
            password=password
        )
        user.merchant = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    """
    Define our User model that inherits from AbstractBaseUser
    """
    username = models.CharField(max_length=120, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    merchant = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        """
        Return an instance representation
        """
        return self.username

    def get_full_name(self):
        """
        Return full name of a user
        """
        return self.email

    def get_short_name(self):
        """
        Return short name of a user
        """
        return self.username

    def has_perm(self, perm, obj=None):
        """
        Check whether a user has a specific permission
        """
        return True

    def has_module_perms(self, app_label):
        """
        Check module level permission
        """
        return True

    @property
    def is_merchant(self):
        """
        Define is_merchant property
        """
        return self.merchant

    @property
    def is_admin(self):
        """
        Define is_admin property
        """
        return self.admin

    @property
    def is_active(self):
        """
        Define is_active property
        """
        return self.active

    @property
    def is_staff(self):
        """
        Define is_staff property
        """
        return self.is_admin
