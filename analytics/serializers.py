from rest_framework import serializers
from analytics.models import CreatorAnalytics, RevenueReport

class AnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreatorAnalytics
        fields = ['creator', 'total_subscribers', 'total_revenue', 'total_courses', 'total_students', 'total_views', 'updated_at']
        
class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueReport
        fields = ['creators', 'month', 'year', 'total_revenue', 'total_subscriptions', 'created_at']