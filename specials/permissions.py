from rest_framework import permissions


class IsAuthenticatedPostPermissions(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == "POST":
            return super().has_permission(request, view)
        return True
