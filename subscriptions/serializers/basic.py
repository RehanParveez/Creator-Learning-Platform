from rest_framework import serializers
from subscriptions.models import Product, Plan, Subscription

class ProductSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description']
        
class PlanSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['name', 'price', 'trial']
        
class SubscriptionSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['user', 'plan', 'status']