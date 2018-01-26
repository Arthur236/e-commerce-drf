from rest_framework import generics, permissions
from django.contrib.auth import get_user_model

from .models import Profile
from .serializers import ProfileSerializer

User = get_user_model()


class ProfileDetailView(generics.RetrieveAPIView):
    """
    View to retrieve a user instance.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
