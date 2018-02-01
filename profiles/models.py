"""
Profile models
"""
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    """
    Define the profile model
    """
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Return a string representation
        """
        return self.user.username


def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    """
    Create a profile after a user is created
    """
    if created:
        # profile, is_created = Profile.objects.get_or_create(user=instance)
        Profile.objects.get_or_create(user=instance)


post_save.connect(post_save_user_receiver, sender=User)
