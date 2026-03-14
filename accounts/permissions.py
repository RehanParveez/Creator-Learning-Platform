from rest_framework.permissions import BasePermission

class PlatformAdminPermission(BasePermission):
  def has_permission(self, request, view):
    return request.user.is_authenticated and request.user.control == 'platformadmin'

  def has_object_permission(self, request, view, obj):
    return request.user.is_authenticated and request.user.control == 'platformadmin'

class CreatorPermission(BasePermission):
  def has_permission(self, request, view):
    return request.user.is_authenticated and request.user.control == 'creator'

  def has_object_permission(self, request, view, obj):
    return request.user.is_authenticated and request.user.control == 'creator' and obj.creator == request.user

class SubscriberPermission(BasePermission):
  def has_permission(self, request, view):
    return request.user.is_authenticated and request.user.control == 'subscriber'

  def has_object_permission(self, request, view, obj):
    return request.user.is_authenticated and request.user.control == 'subscriber'



