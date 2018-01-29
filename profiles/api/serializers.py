from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfileSerializer(serializers.Serializer):
    """
    This serializer combines data from user and profile model
    """

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    username = serializers.CharField(max_length=120)
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=120)
    last_name = serializers.CharField(max_length=120)
    last_login = serializers.DateTimeField(allow_null=True)
    date_created = serializers.DateTimeField()
