"""
Accounts serializer
"""
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer
    """
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, min_length=8)

    class Meta:
        """
        Specify meta data
        """
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        """
        Create a user
        """
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user

    def validate_username(self, value):
        """
        Validates username
        """
        qs = User.objects.filter(username__iexact=value)

        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("That username is already taken.")
        return value

    def validate_email(self, value):
        """
        Validates email
        """
        qs = User.objects.filter(email__iexact=value)

        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("That email is already taken.")
        return value


class MerchantSerializer(serializers.ModelSerializer):
    """
    Merchant serializer
    """
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, min_length=8)

    class Meta:
        """
        Specify meta data
        """
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        """
        Create a merchant
        """
        user = User.objects.create_merchant(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )

        return user

    def validate_username(self, value):
        """
        Validates username
        """
        qs = User.objects.filter(username__iexact=value)

        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("That username is already taken.")
        return value

    def validate_email(self, value):
        """
        Validates email
        """
        qs = User.objects.filter(email__iexact=value)

        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("That email is already taken.")
        return value


class TokenSerializer(serializers.Serializer):
    """
    Serializes the token data
    """

    def update(self, instance, validated_data):
        """
        Update method
        """
        pass

    def create(self, validated_data):
        """
        Create method
        """
        pass

    token = serializers.CharField(max_length=255)
