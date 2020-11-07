from rest_framework import permissions


class IsClient(permissions.BasePermission):
    ''' Является ли пользователь клиентом '''

    def has_object_permission(self, request, view, obj):
        return request.user.role == 'CL'
