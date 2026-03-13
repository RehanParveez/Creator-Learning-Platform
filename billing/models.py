from django.db import models
from subscriptions.models import Subscription
from accounts.models import User

# Create your models here.
class Invoice(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
    )
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name = 'invoices')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'invoices')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default = 'pending')
    given_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    paid_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.id} {self.user}'
    
class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name = 'items')
    description = models.CharField(max_length=60)
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.description
    
class PaymentMethod(models.Model):
    TYPE_CHOICES = (
        ('stripe', 'Stripe'),
        ('paypal', 'Paypal'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'payment_methods')
    method_type = models.CharField(max_length=45, choices=TYPE_CHOICES)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.method_type
    
class Payment(models.Model):
    STATUS_CHOICES = (
        ('success', 'Success'),
        ('failed', 'Failed'),
        ('pending', 'Pending'),
    )
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name = 'payments')
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=45, choices=STATUS_CHOICES)
    paid_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.id} {self.status}'
    
    
