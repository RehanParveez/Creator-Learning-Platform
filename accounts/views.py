from django.shortcuts import render
from rest_framework import viewsets
from accounts.serializers.detail import UserSerializer, FollowerSerializer
from accounts.models import User, Follower
from accounts.permissions import PlatformAdminPermission, SubscriberPermission
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [PlatformAdminPermission]
    
    def get_queryset(self):
        user = self.request.user
        if user.control == 'platformadmin':
            return self.queryset
        return self.queryset.none()

class FollowerViewset(viewsets.ModelViewSet):
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
    permission_classes = [SubscriberPermission, IsAuthenticated]
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      if user.control == 'subscriber':
        return self.queryset.filter(follower=user)
      if user.control == 'creator':
        return self.queryset.filter(creator__user=user)
    
      return self.queryset.none()
    