from rest_framework import serializers

from profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'user',
            'first_name',
            'last_name',
            'timestamp',
            'updated'
        )

        read_only_fields = ['user']
