from django.shortcuts import render
from rest_framework import viewsets
from billing.serializers.detail import InvoiceSerializer, InvoiceItemSerializer, PaymentMethodSerializer, PaymentSerializer
from billing.models import Invoice, InvoiceItem, PaymentMethod, Payment
from accounts.permissions import PlatformAdminPermission, SubscriberPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.
class InvoiceViewset(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all().order_by('id')
    permission_classes = [PlatformAdminPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['amount']
    ordering_fields = ['paid_at']
    filterset_fields = ['status', 'due_date', 'paid_at']
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      if user.control == 'subscriber':
        return self.queryset.filter(user=user)
      if user.control == 'creator':
        return self.queryset.filter(subscription__plan__product__creator__user=user)

      return self.queryset.none()

class InvoiceItemViewset(viewsets.ModelViewSet):
    serializer_class = InvoiceItemSerializer
    queryset = InvoiceItem.objects.all().order_by('id')
    permission_classes = [PlatformAdminPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['amount']
    ordering_fields = ['amount']
    filterset_fields = ['amount', 'description']
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      if user.control == 'subscriber':
        return self.queryset.filter(invoice__user=user)
      if user.control == 'creator':
        return self.queryset.filter(invoice__subscription__plan__product__creator__user=user)

      return self.queryset.none()
    
class PaymentMethodViewset(viewsets.ModelViewSet):
    serializer_class = PaymentMethodSerializer
    queryset = PaymentMethod.objects.all().order_by('id')
    permission_classes = [SubscriberPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['method_type']
    ordering_fields = ['created_at']
    filterset_fields = ['is_default', 'created_at']
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      return self.queryset.filter(user=user)
    
class PaymentViewset(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all().order_by('id')
    permission_classes = [SubscriberPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['amount']
    ordering_fields = ['paid_at']
    filterset_fields = ['status', 'paid_at']
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      if user.control == 'subscriber':
        return self.queryset.filter(invoice__user=user)
      if user.control == 'creator':
        return self.queryset.filter(invoice__subscription__plan__product__creator__user=user)
    
      return self.queryset.none()