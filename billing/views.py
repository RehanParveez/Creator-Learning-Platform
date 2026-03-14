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

class InvoiceItemViewset(viewsets.ModelViewSet):
    serializer_class = InvoiceItemSerializer
    queryset = InvoiceItem.objects.all()
    permission_classes = [PlatformAdminPermission]
    
class PaymentMethodViewset(viewsets.ModelViewSet):
    serializer_class = PaymentMethodSerializer
    queryset = PaymentMethod.objects.all()
    permission_classes = [SubscriberPermission]
    
class PaymentViewset(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [SubscriberPermission]