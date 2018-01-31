from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticated
)

from ecommerce.permissions import IsOwnerOrReadOnly
from profiles.models import Profile
from .serializers import ProfileSerializer

User = get_user_model()


class UserProfileRUpView(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a user's profile.
    """
    lookup_field = 'username'
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return User.objects.all()
