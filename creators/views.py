from django.shortcuts import render
from rest_framework import viewsets
from creators.serializers.detail import CreatorProfileSerializer
from creators.models import CreatorProfile
from accounts.permissions import CreatorPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.
class CreatorsViewset(viewsets.ModelViewSet):
    serializer_class = CreatorProfileSerializer
    queryset = CreatorProfile.objects.all().order_by('id')
    permission_classes = [CreatorPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['name', 'bio', 'courses']
    ordering_fields = ['created_at']
    filterset_fields = ['name', 'courses', 'is_verified', 'updated_at', 'created_at']
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      if user.control == 'creator':
        return self.queryset.filter(user=user)

      return self.queryset
