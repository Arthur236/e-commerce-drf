from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, min_length=8)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user

    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)

        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("That username is already taken.")
        return value

    def validate_email(self, value):
        qs = User.objects.filter(email__iexact=value)

        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("That email is already taken.")
        return value


class MerchantSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, min_length=8)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_merchant(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )

        return user

    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)

        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("That username is already taken.")
        return value

    def validate_email(self, value):
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
        pass

    def create(self, validated_data):
        pass

    token = serializers.CharField(max_length=255)
