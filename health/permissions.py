# -*- coding: utf-8 -*-

from rest_framework.permissions import BasePermission


class IsZoneOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.owner_id


class IsNodeOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.zone.owner_id
