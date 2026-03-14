from django.shortcuts import render
from rest_framework import viewsets
from accounts.serializers.detail import UserSerializer, FollowerSerializer
from accounts.models import User, Follower
from accounts.permissions import PlatformAdminPermission, SubscriberPermission

# Create your views here.
class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [PlatformAdminPermission]

class FollowerViewset(viewsets.ModelViewSet):
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
    permission_classes = [SubscriberPermission]
    