from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'],
                                        validated_data['first_name'],
                                        validated_data['last_name'],
                                        validated_data['password']
                                        )
        return user

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
