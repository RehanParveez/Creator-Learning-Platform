from django.shortcuts import render
from rest_framework import viewsets
from subscriptions.serializers.detail import ProductSerializer, PlanSerializer, SubscriptionSerializer, CouponSerializer
from subscriptions.models import Product, Plan, Subscription, Coupon
from accounts.permissions import CreatorPermission, SubscriberPermission, PlatformAdminPermission
from subscriptions.services import create_sub
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.
class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by('id')
    permission_classes = [CreatorPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['name', 'description']
    ordering_fields = ['created_at']
    filterset_fields = ['name', 'is_active', 'created_at']
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      if user.control == 'creator':
         return self.queryset.filter(creator__user=user)

      return self.queryset.none()

class PlanViewset(viewsets.ModelViewSet):
    serializer_class = PlanSerializer
    queryset = Plan.objects.all().order_by('id')
    permission_classes = [CreatorPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['name', 'price']
    ordering_fields = ['created_at']
    filterset_fields = ['billing', 'trial', 'is_active', 'created_at']
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      if user.control == 'creator':
        return self.queryset.filter(product__creator__user=user)

      return self.queryset.none()
    
class SubscriptionViewset(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all().order_by('id')
    permission_classes = [SubscriberPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['status']
    ordering_fields = ['created_at']
    filterset_fields = ['status', 'started_at', 'canceled_at', 'created_at']
    
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
    queryset = Coupon.objects.all().order_by('id')
    permission_classes = [PlatformAdminPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['discount']
    ordering_fields = ['valid_from']
    filterset_fields = ['valid_from', 'valid_until', 'is_active']
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      return self.queryset.none()