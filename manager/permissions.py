from rest_framework import permissions


class IsManager(permissions.BasePermission):
    ''' Является ли пользователь менеджером '''

    def has_object_permission(self, request, view, obj):
        return request.user.role == 'MN'