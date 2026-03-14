from django.shortcuts import render
from rest_framework import viewsets
from subscriptions.serializers import ProductSerializer, PlanSerializer, SubscriptionSerializer, CouponSerializer
from subscriptions.models import Product, Plan, Subscription, Coupon

# Create your views here.
class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class PlanViewset(viewsets.ModelViewSet):
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()
    
class SubscriptionViewset(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    
class CouponViewset(viewsets.ModelViewSet):
    serializer_class = CouponSerializer
    queryset = Coupon.objects.all()