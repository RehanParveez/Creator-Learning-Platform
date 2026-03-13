from django.contrib import admin
from analytics.models import CreatorAnalytics, RevenueReport

# Register your models here.
@admin.register(CreatorAnalytics)
class AnalyticsAdmin(admin.ModelAdmin):
    list_display = ['creator', 'total_subscribers', 'total_revenue', 'total_courses', 'total_students', 'total_views', 'updated_at']
    
@admin.register(RevenueReport)
class RevenueAdmin(admin.ModelAdmin):
    list_display = ['creators', 'month', 'year', 'total_revenue', 'total_subscriptions', 'created_at']
    

