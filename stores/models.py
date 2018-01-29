from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Store(models.Model):
    user = models.OneToOneField(User)  # user.profile
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
