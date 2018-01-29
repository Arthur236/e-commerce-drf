from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import (
    IsAuthenticated
)
from rest_framework.response import Response

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings

from profiles.utils import (
    get_profile,
    user_is_allowed
)
from.serializers import UserProfileSerializer


class UserProfileDetails(RetrieveUpdateAPIView):
    """
    Retrieve, update or delete a user's profile.
    """
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None, **kwargs):
        """
        Retrieve user profile of the user in the request object
        """
        username = kwargs['username']

        if user_is_allowed(request, username):
            data = get_profile(username=username)
            if data is not None:
                serializer = UserProfileSerializer(data=data)
                serializer.is_valid()
                return Response(data=serializer.data)
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    # def put(self, request, format=None, **kwargs):
    #     """
    #     Update user profile
    #     """
    #     username = kwargs['username']
    #     if user_is_allowed(request, username):
    #         data = {
    #             'username': username,
    #             'email': request.data.get('email', ''),
    #             'first_name': request.data.get('first_name', ''),
    #             'last_name': request.data.get('last_name', ''),
    #             'description': request.data.get('description', '')
    #         }
    #         if update_user_profile(data=data):
    #             serializer = UserProfileSerializer(
    #                 data=get_profile(
    #                     username=request.user.username
    #                 )
    #             )
    #             serializer.is_valid()
    #             return Response(data=serializer.data)
    #         return Response(status=status.HTTP_400_BAD_REQUEST)
    #     return Response(status=status.HTTP_401_UNAUTHORIZED)
