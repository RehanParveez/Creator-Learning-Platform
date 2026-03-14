from django.shortcuts import render
from rest_framework import viewsets
from subscriptions.serializers.detail import ProductSerializer, PlanSerializer, SubscriptionSerializer, CouponSerializer
from subscriptions.models import Product, Plan, Subscription, Coupon
from accounts.permissions import CreatorPermission, SubscriberPermission, PlatformAdminPermission

# Create your views here.
class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [CreatorPermission]

class PlanViewset(viewsets.ModelViewSet):
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()
    permission_classes = [CreatorPermission]
    
class SubscriptionViewset(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [SubscriberPermission]
    
class CouponViewset(viewsets.ModelViewSet):
    serializer_class = CouponSerializer
    queryset = Coupon.objects.all()
    permission_classes = [PlatformAdminPermission]