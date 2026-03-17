from django.shortcuts import render
from rest_framework import viewsets
from analytics.serializers import AnalyticsSerializer, RevenueSerializer
from analytics.models import CreatorAnalytics, RevenueReport
from accounts.permissions import CreatorPermission, PlatformAdminPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.
class AnalyticsViewset(viewsets.ModelViewSet):
    serializer_class = AnalyticsSerializer
    queryset = CreatorAnalytics.objects.all()
    permission_classes = [CreatorPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['total_courses']
    ordering_fields = ['updated_at']
    filterset_fields = ['total_students', 'total_courses', 'total_views', 'updated_at']
    
    def get_queryset(self):
      user = self.request.user
      
      if user.control == 'creator':
        return self.queryset.filter(creator__user=user)
      return self.queryset
    
class RevenueViewset(viewsets.ModelViewSet):
    serializer_class = RevenueSerializer
    queryset = RevenueReport.objects.all()
    permission_classes = [PlatformAdminPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['month']
    ordering_fields = ['created_at']
    filterset_fields = ['month', 'year', 'created_at']
    
    def get_queryset(self):
      user = self.request.user
      
      if user.control == 'creator':
        return self.queryset.filter(creators__user=user)
      return self.queryset