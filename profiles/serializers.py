from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    A user profile serializer.
    """

    class Meta:
        """Map this serializer to the default django user model."""
        model = Profile
        fields = ('id',
                  'user',
                  'first_name',
                  'last_name',
                  'timestamp',
                  'updated')
