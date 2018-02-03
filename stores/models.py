"""
Store models
"""
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save

from ecommerce.utils import unique_slug_generator

User = settings.AUTH_USER_MODEL


class Store(models.Model):
    """
    Define the store model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Define unique fields
        """
        unique_together = ('user', 'name')

    def __str__(self):
        """
        Return string representation of an instance
        """
        return self.name


def rl_pre_save_receiver(sender, instance, **kwargs):
    """
    Generate a unique slug after a store is saved
    """
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(rl_pre_save_receiver, sender=Store)
