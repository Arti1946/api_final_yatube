from rest_framework import permissions


class UserActionsPermisiion(permissions.BasePermission):
    message = "Изменять или удалять чужие записи запрещено"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
