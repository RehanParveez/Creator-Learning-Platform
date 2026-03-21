from rest_framework.permissions import BasePermission

class PlatformAdminPermission(BasePermission):
  def has_permission(self, request, view):
    user = request.user
    return user and user.is_authenticated and user.control == 'platformadmin'

  def has_object_permission(self, request, view, obj):
    user = request.user
    return user and user.is_authenticated and user.control == 'platformadmin'

class CreatorPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False
        if user.control == 'platformadmin':
            return True
        return user.control == 'creator'

    def has_object_permission(self, request, view, obj):
        user = request.user

        if user.control == 'platformadmin':
            return True
        return obj.product.creator.user == user

class SubscriberPermission(BasePermission):
  def has_permission(self, request, view):
      user = request.user
      
      if not user or not user.is_authenticated:
        return False
      if user.control == 'platformadmin':
        return True
      return user.control == 'subscriber'

  def has_object_permission(self, request, view, obj):
      user = request.user  
      
      if user.control == 'platformadmin':
          return True
      return user.control == 'subscriber'
  