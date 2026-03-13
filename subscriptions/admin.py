from django.contrib import admin
from subscriptions.models import Product, Plan, Subscription, Coupon

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['creator', 'name', 'description', 'is_active', 'created_at']
    
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['product', 'name', 'price', 'billing', 'trial', 'is_active', 'created_at']
    
@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'plan', 'status', 'started_at', 'expires_at', 'canceled_at', 'created_at']
    
@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount', 'valid_from', 'valid_until', 'is_active']
