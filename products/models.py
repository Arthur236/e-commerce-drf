"""
Product models
"""
from django.db import models
from django.db.models.signals import pre_save

from ecommerce.utils import unique_slug_generator
from stores.models import Store


class Product(models.Model):
    """
    Define product model
    """
    store = models.OneToOneField(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Specify meta data
        """
        unique_together = ('store', 'name')

    def __str__(self):
        """
        Return string representation of instance
        """
        return self.name


def rl_pre_save_receiver(sender, instance, **kwargs):
    """
    Generate unique slug after product is created
    """
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(rl_pre_save_receiver, sender=Store)
