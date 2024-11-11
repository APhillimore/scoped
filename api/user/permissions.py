from user.authentication import get_user_claims
from rest_framework import permissions
from django.conf import settings


class DenyAny(permissions.BasePermission):
    def has_permission(self, request, view):
        return False

    def has_object_permission(self, request, view, obj):
        return False


class IsCognitoAuthenticated(DenyAny):
    def has_permission(self, request, view):
        if settings.DISABLE_AUTH:
            return True
        claims = get_user_claims(request)
        if not claims:
            return False
        return True

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
