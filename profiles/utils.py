from django.contrib.auth import get_user_model

from .models import Profile

User = get_user_model()


def user_is_allowed(request, username):
    """
    Checks if the user has permission to access a resource
    """
    return request.user.username == username or request.user.is_admin


def get_profile(username):
    """
    Fetch a user's profile
    """
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return None

    profile = Profile.objects.get(user=user)

    data = {
        'username': user.username,
        'email': user.email,
        'first_name': profile.first_name,
        'last_name': profile.last_name,
        'last_login': user.last_login,
        'date_created': user.date_created
    }

    return data
