from django.contrib import admin
from billing.models import Invoice, InvoiceItem, PaymentMethod, Payment

# Register your models here.
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['subscription', 'user', 'amount', 'status', 'given_at', 'due_date', 'paid_at']
    
@admin.register(InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ['invoice', 'description', 'amount']
    
@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ['user', 'method_type', 'is_default', 'created_at']
    
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['invoice', 'payment_method', 'amount', 'status', 'paid_at']