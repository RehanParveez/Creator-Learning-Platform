from django.db import models
from creators.models import CreatorProfile
from accounts.models import User

# Create your models here.
class Product(models.Model):
    creator = models.ForeignKey(CreatorProfile, on_delete=models.CASCADE, related_name = 'products')
    name = models.CharField(max_length=55)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Plan(models.Model):
    BILLING_CHOICES = (
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = 'plans')
    name = models.CharField(max_length=55)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    billing = models.CharField(max_length=45, choices=BILLING_CHOICES)
    trial = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Subscription(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('canceled', 'Canceled'),
        ('expired', 'Expired'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'subscriptions')
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    status = models.CharField(max_length=45, choices=STATUS_CHOICES)
    started_at = models.DateTimeField()
    expires_at = models.DateTimeField()
    canceled_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.status
    
class Coupon(models.Model):
    code = models.CharField(max_length=55, unique=True)
    discount = models.IntegerField()
    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.discount
