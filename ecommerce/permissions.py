"""
Custom permissions
"""
from django.contrib.auth import get_user_model
from rest_framework import permissions

User = get_user_model()


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object level permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        """
        Read permissions are allowed to any request
        """
        if request.method in permissions.SAFE_METHODS or request.user.is_admin:
            return True

        # Compare instance to the user in request
        return obj.user == request.user


class IsMerchant(permissions.BasePermission):
    """
    Check whether the user is a merchant
    """
    def has_permission(self, request, view):
        """
        Read permissions are allowed to any request
        """
        if request.user.merchant:
            return True

        return False


class IsStoreOwner(permissions.BasePermission):
    """
    Check whether a user is the owner of store
    """
    def has_object_permission(self, request, view, obj):
        """
        Read permissions are allowed to any request
        """
        if request.user.merchant and obj.store.user == request.user:
            return True

        return False
