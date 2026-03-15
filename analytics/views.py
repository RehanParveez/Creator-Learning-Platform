from django.shortcuts import render
from rest_framework import viewsets
from analytics.serializers import AnalyticsSerializer, RevenueSerializer
from analytics.models import CreatorAnalytics, RevenueReport
from accounts.permissions import CreatorPermission, PlatformAdminPermission

# Create your views here.
class AnalyticsViewset(viewsets.ModelViewSet):
    serializer_class = AnalyticsSerializer
    queryset = CreatorAnalytics.objects.all()
    permission_classes = [CreatorPermission]
    
    def get_queryset(self):
      user = self.request.user
      
      if user.control == 'creator':
        return self.queryset.filter(creator__user=user)
      return self.queryset
    
class RevenueViewset(viewsets.ModelViewSet):
    serializer_class = RevenueSerializer
    queryset = RevenueReport.objects.all()
    permission_classes = [PlatformAdminPermission]
    
    def get_queryset(self):
      user = self.request.user
      
      if user.control == 'creator':
        return self.queryset.filter(creators__user=user)
      return self.queryset