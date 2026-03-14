from django.shortcuts import render
from rest_framework import viewsets
from accounts.serializers import UserSerializer, FollowerSerializer
from accounts.models import User, Follower

# Create your views here.
class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class FollowerViewset(viewsets.ModelViewSet):
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()