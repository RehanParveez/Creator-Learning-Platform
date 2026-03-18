from django.db import transaction
from subscriptions.models import Plan, Subscription
from django.utils import timezone
from billing.models import Invoice, InvoiceItem, PaymentMethod, Payment
from datetime import timedelta
from engagement.models import Activity

@transaction.atomic
def create_sub(user, plan_id, pay_method_id):
  print('the service of sub is working')
  plan = Plan.objects.get(id=plan_id)
  pay_method = PaymentMethod.objects.get(id=pay_method_id, user=user)
  now = timezone.now()
  
  if plan.billing == 'monthly':
    expires = now + timedelta(days = 30)
  else:
    expires = now + timedelta(days = 365)
      
  subscription = Subscription.objects.create(user=user, plan=plan, status = 'is_active', started_at=now, expires_at=expires)
  invoice = Invoice.objects.create(subscription=subscription, user=user, amount=plan.price, status = 'pending', due_date=now)
  InvoiceItem.objects.create(invoice=invoice, description=plan.name, amount=plan.price)
  Payment.objects.create(invoice=invoice, payment_method=pay_method, amount=plan.price, status = 'success', paid_at = now)
  
  invoice.status = 'paid'
  invoice.paid_at = now
  invoice.save()
  
  Activity.objects.create(user=user, work=f'subscription {plan.name}')
  return subscription
  