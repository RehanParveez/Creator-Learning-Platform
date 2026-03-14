from rest_framework import serializers
from billing.models import Invoice, InvoiceItem, PaymentMethod, Payment

class InvoiceItemSerializer1(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = ['invoice']
        
class InvoiceSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['amount', 'status', 'paid_at']

class PaymentMethodSerializer1(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['user', 'method_type']
        
class PaymentSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['amount', 'status']