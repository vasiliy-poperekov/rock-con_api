from rest_framework.permissions import BasePermission


class IsGroupSingerUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_group_singer)


class IsPlaceUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_place)
