from django.shortcuts import render
from rest_framework import viewsets
from subscriptions.serializers.detail import ProductSerializer, PlanSerializer, SubscriptionSerializer, CouponSerializer
from subscriptions.models import Product, Plan, Subscription, Coupon
from accounts.permissions import CreatorPermission, SubscriberPermission, PlatformAdminPermission
from subscriptions.services import create_sub
from rest_framework.response import Response

# Create your views here.
class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [CreatorPermission]
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      if user.control == 'creator':
         return self.queryset.filter(creator__user=user)

      return self.queryset.none()

class PlanViewset(viewsets.ModelViewSet):
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()
    permission_classes = [CreatorPermission]
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      if user.control == 'creator':
        return self.queryset.filter(product__creator__user=user)

      return self.queryset.none()
    
class SubscriptionViewset(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [SubscriberPermission]
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      if user.control == 'subscriber':
        return self.queryset.filter(user=user)
      if user.control == 'creator':
        return self.queryset.filter(plan__product__creator__user=user)

      return self.queryset.none()
    
    def create(self, request):
      plan_id = request.data.get('plan_id')
      pay_method_id = request.data.get('pay_method_id')
      
      subscription = create_sub(user=request.user, plan_id=plan_id, pay_method_id=pay_method_id)
      serializer = self.get_serializer(subscription)
      return Response(serializer.data, status=201)
    
class CouponViewset(viewsets.ModelViewSet):
    serializer_class = CouponSerializer
    queryset = Coupon.objects.all()
    permission_classes = [PlatformAdminPermission]
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      return self.queryset.none()