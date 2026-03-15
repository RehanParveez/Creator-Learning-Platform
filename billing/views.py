from django.shortcuts import render
from rest_framework import viewsets
from billing.serializers.detail import InvoiceSerializer, InvoiceItemSerializer, PaymentMethodSerializer, PaymentSerializer
from billing.models import Invoice, InvoiceItem, PaymentMethod, Payment
from accounts.permissions import PlatformAdminPermission, SubscriberPermission

# Create your views here.
class InvoiceViewset(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
    permission_classes = [PlatformAdminPermission]
    
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
    queryset = InvoiceItem.objects.all()
    permission_classes = [PlatformAdminPermission]
    
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
    queryset = PaymentMethod.objects.all()
    permission_classes = [SubscriberPermission]
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      return self.queryset.filter(user=user)
    
class PaymentViewset(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [SubscriberPermission]
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      if user.control == 'subscriber':
        return self.queryset.filter(invoice__user=user)
      if user.control == 'creator':
        return self.queryset.filter(invoice__subscription__plan__product__creator__user=user)
    
      return self.queryset.none()