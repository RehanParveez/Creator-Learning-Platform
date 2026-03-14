from django.shortcuts import render
from rest_framework import viewsets
from analytics.serializers import AnalyticsSerializer, RevenueSerializer
from analytics.models import CreatorAnalytics, RevenueReport

# Create your views here.
class AnalyticsViewset(viewsets.ModelViewSet):
    serializer_class = AnalyticsSerializer
    queryset = CreatorAnalytics.objects.all()
    
class RevenueViewset(viewsets.ModelViewSet):
    serializer_class = RevenueSerializer
    queryset = RevenueReport.objects.all()