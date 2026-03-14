from rest_framework import serializers
from subscriptions.models import Product, Plan, Subscription, Coupon

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['creator', 'name', 'description', 'is_active', 'created_at']
        
class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['product', 'name', 'price', 'billing', 'trial', 'is_active', 'created_at']
        
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['user', 'plan', 'status', 'started_at', 'expires_at', 'canceled_at', 'created_at']
        
class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['code', 'discount', 'valid_from', 'valid_until', 'is_active']