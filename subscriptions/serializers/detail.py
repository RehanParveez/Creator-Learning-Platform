from rest_framework import serializers
from subscriptions.models import Product, Plan, Subscription, Coupon
from creators.serializers.basic import CreatorProfileSerializer1
from accounts.serializers.basic import UserSerializer1
from subscriptions.serializers.basic import PlanSerializer1
from subscriptions.serializers.basic import ProductSerializer1
   
class ProductSerializer(serializers.ModelSerializer):
    creator = CreatorProfileSerializer1(read_only=True)
    plans = PlanSerializer1(many=True)
    class Meta:
        model = Product
        fields = ['creator', 'name', 'description', 'plans', 'is_active', 'created_at']
        
class PlanSerializer(serializers.ModelSerializer):
    product = ProductSerializer1(read_only=True)
    class Meta:
        model = Plan
        fields = ['product', 'name', 'price', 'billing', 'trial', 'is_active', 'created_at']
          
class SubscriptionSerializer(serializers.ModelSerializer):
    user = UserSerializer1(read_only=True)
    plan = PlanSerializer1(read_only=True)
    class Meta:
        model = Subscription
        fields = ['user', 'plan', 'status', 'started_at', 'expires_at', 'canceled_at', 'created_at']
        
class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['code', 'discount', 'valid_from', 'valid_until', 'is_active']