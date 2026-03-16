from rest_framework import serializers
from analytics.models import CreatorAnalytics, RevenueReport
from creators.serializers.basic import CreatorProfileSerializer1

class AnalyticsSerializer(serializers.ModelSerializer):
    creator = CreatorProfileSerializer1(read_only=True)
    class Meta:
        model = CreatorAnalytics
        fields = ['creator', 'total_subscribers', 'total_revenue', 'total_courses', 'total_students', 'total_views', 'updated_at']
        
class RevenueSerializer(serializers.ModelSerializer):
    creator = CreatorProfileSerializer1(read_only=True)
    class Meta:
        model = RevenueReport
        fields = ['creator', 'month', 'year', 'total_revenue', 'total_subscriptions', 'created_at']