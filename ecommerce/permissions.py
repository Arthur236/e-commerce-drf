from rest_framework import permissions


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

        # Compare instance attribute to the user in request
        return obj.user == request.user
