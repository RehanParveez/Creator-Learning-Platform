from django.shortcuts import render
from rest_framework import viewsets
from engagement.serializers.detail import CommentSerializer, LikeSerializer, ActivitySerializer
from engagement.models import Comment, Like, Activity
from accounts.permissions import SubscriberPermission, PlatformAdminPermission

# Create your views here.
class CommentViewset(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [SubscriberPermission]
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      if user.control == 'subscriber':
        return self.queryset.filter(user=user)
      if user.control == 'creator':
        return self.queryset.filter(lesson__section__course__creator__user=user)

      return self.queryset.none()
    
class LikeViewset(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    permission_classes = [SubscriberPermission]
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      if user.control == 'subscriber':
        return self.queryset.filter(user=user)
      if user.control == 'creator':
        return self.queryset.filter(lesson__section__course__creator__user=user)

      return self.queryset.none()
    
class ActivityViewset(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
    permission_classes = [PlatformAdminPermission]
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      return self.queryset.none()