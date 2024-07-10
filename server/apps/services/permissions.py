from rest_framework.permissions import BasePermission


class IsCreatorOrStaffPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user or request.user.is_staff


class IsStaffPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
