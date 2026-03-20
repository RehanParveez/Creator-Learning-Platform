from django.shortcuts import render
from rest_framework import viewsets
from accounts.serializers.detail import UserSerializer, FollowerSerializer, RegisterSerializer
from accounts.models import User, Follower
from accounts.permissions import PlatformAdminPermission, SubscriberPermission
from rest_framework.views import APIView
from accounts.serializers.detail import RegisterSerializer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.
class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('id')
    permission_classes = [PlatformAdminPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['email']
    ordering_fields = ['created_at']
    filterset_fields = ['dob', 'is_active', 'is_staff', 'updated_at', 'created_at']
    
    def get_queryset(self):
        user = self.request.user
        if user.control == 'platformadmin':
            return self.queryset
        return self.queryset.none()

class FollowerViewset(viewsets.ModelViewSet):
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all().order_by('id')
    permission_classes = [SubscriberPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['created_at']
    ordering_fields = ['created_at']
    filterset_fields = ['updated_at', 'created_at']
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      if user.control == 'subscriber':
        return self.queryset.filter(follower=user)
      if user.control == 'creator':
        return self.queryset.filter(creator__user=user)
    
      return self.queryset.none()

class RegisterView(APIView):
  def post(self, request):
    
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
  
  
    