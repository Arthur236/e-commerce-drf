from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    first_name = serializers.CharField(source='user_profile.first_name', allow_blank=True, allow_null=True)
    last_name = serializers.CharField(source='user_profile.last_name', allow_blank=True, allow_null=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'last_login',
            'first_name',
            'last_name',
            'date_created',
            'updated'
        )

        read_only_fields = ['last_login', 'date_created']
