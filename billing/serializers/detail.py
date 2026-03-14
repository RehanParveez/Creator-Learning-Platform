from rest_framework import serializers
from billing.models import Invoice, InvoiceItem, PaymentMethod, Payment
from subscriptions.serializers.basic import SubscriptionSerializer1
from accounts.serializers.basic import UserSerializer1
from billing.serializers.basic import InvoiceItemSerializer1, InvoiceSerializer1, PaymentSerializer1, PaymentMethodSerializer1

class InvoiceSerializer(serializers.ModelSerializer):
    subscription = SubscriptionSerializer1(read_only=True)
    user = UserSerializer1(read_only=True)
    items = InvoiceItemSerializer1(many=True)
    payments = PaymentSerializer1(many=True)
    class Meta:
        model = Invoice
        fields = ['subscription', 'user', 'amount', 'status', 'items', 'payments', 'given_at', 'due_date', 'paid_at']
             
class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = ['invoice', 'description', 'amount']
        
class PaymentMethodSerializer(serializers.ModelSerializer):
    user = UserSerializer1(read_only=True)
    class Meta:
        model = PaymentMethod
        fields = ['user', 'method_type', 'is_default', 'created_at']
        
class PaymentSerializer(serializers.ModelSerializer):
    invoice = InvoiceSerializer1(read_only=True)
    payment_method = PaymentMethodSerializer1(read_only=True)
    class Meta:
        model = Payment
        fields = ['invoice', 'payment_method', 'amount', 'status', 'paid_at']
        