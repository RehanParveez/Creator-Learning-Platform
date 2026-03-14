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
    
class LikeViewset(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    permission_classes = [SubscriberPermission]
    
class ActivityViewset(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
    permission_classes = [PlatformAdminPermission]