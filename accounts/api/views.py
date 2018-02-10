"""
Accounts api views
"""
from django.contrib.auth import get_user_model, authenticate, login, logout

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import (
    IsAuthenticated
)

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings

from .serializers import (
    MerchantSerializer,
    UserSerializer
)

User = get_user_model()

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class RegisterAPIView(APIView):
    """
    Registers a new user
    """
    def post(self, request):
        """
        Define post method logic
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                response = serializer.data
                response['token'] = token.key
                return Response(response, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MerchantRegisterAPIView(APIView):
    """
    Registers a new merchant
    """
    def post(self, request):
        """
        Define post method logic
        """
        serializer = MerchantSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                response = serializer.data
                response['token'] = token.key
                return Response(response, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    Logs in a user
    """
    queryset = User.objects.all()

    def get_user(self, email):
        """
        Function to resolve email to username
        """
        try:
            return User.objects.get(email=email.lower())
        except User.DoesNotExist:
            return None

    def post(self, request, **kwargs):
        """
        Define post method logic
        """
        email = request.data.get('email', '')
        password = request.data.get('password', '')
        username = self.get_user(email)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Save the user’s ID in the session, using Django’s session framework.
            login(request, user)
            response = {
                # Using drf jwt utility functions to generate a token
                'token': jwt_encode_handler(jwt_payload_handler(user)),
                'user': {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "admin": user.admin,
                    "merchant": user.merchant
                }
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    """
    View to logout a user
    """
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = User.objects.all()

    def get(self, request, **kwargs):
        """
        Define get method logic
        """
        logout(request)
        return Response(status=status.HTTP_200_OK)
