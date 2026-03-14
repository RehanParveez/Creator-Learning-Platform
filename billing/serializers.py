from rest_framework import serializers
from billing.models import Invoice, InvoiceItem, PaymentMethod, Payment

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['subscription', 'user', 'amount', 'status', 'given_at', 'due_date', 'paid_at']
        
class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = ['invoice', 'description', 'amount']
        
class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['user', 'method_type', 'is_default', 'created_at']
        
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['invoice', 'payment_method', 'amount', 'status', 'paid_at']