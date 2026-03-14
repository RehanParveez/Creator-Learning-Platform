from django.shortcuts import render
from rest_framework import viewsets
from billing.serializers import InvoiceSerializer, InvoiceItemSerializer, PaymentMethodSerializer, PaymentSerializer
from billing.models import Invoice, InvoiceItem, PaymentMethod, Payment

# Create your views here.
class InvoiceViewset(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()

class InvoiceItemViewset(viewsets.ModelViewSet):
    serializer_class = InvoiceItemSerializer
    queryset = InvoiceItem.objects.all()
    
class PaymentMethodViewset(viewsets.ModelViewSet):
    serializer_class = PaymentMethodSerializer
    queryset = PaymentMethod.objects.all()
    
class PaymentViewset(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()