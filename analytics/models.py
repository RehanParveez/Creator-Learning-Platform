from django.db import models
from creators.models import CreatorProfile

# Create your models here.
class CreatorAnalytics(models.Model):
    creator = models.OneToOneField(CreatorProfile, on_delete=models.CASCADE, related_name = 'analytics')
    total_subscribers = models.PositiveIntegerField(default=0)
    total_revenue = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_courses = models.PositiveIntegerField(default=0)
    total_students = models.PositiveIntegerField(default=0)
    total_views = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.creator}'
    
class RevenueReport(models.Model):
    creators = models.ForeignKey(CreatorProfile, on_delete=models.CASCADE, related_name = 'revenue_reports')
    month = models.IntegerField()
    year = models.IntegerField()
    total_revenue = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_subscriptions = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.creators}: {self.month}/{self.year}'
