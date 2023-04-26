from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    """Предоставляет права к объекту: безопасные методы запроса
    доступны всем пользователям, а опасные только автору объекта."""
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
