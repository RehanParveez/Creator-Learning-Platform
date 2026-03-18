from celery import shared_task
from django.utils import timezone
from creators.models import CreatorProfile
from subscriptions.models import Subscription
from billing.models import Invoice
from django.db.models import Sum
from analytics.models import RevenueReport, CreatorAnalytics
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def monthly_report():
  now = timezone.now()
  
  if now.month == 1:
    month = 12
    year = now.year - 1
  else:
    month = now.month - 1
    year = now.year
    
  for creator in CreatorProfile.objects.all():
    subscriptions = Subscription.objects.filter(plan__product__creator=creator, status = 'active', started_at__year=year, started_at__month=month)
    total_subscriptions = subscriptions.count()
    
    invoices = Invoice.objects.filter(subscription__in=subscriptions, status = 'paid', paid_at__year=year, paid_at__month=month)
    total = invoices.aggregate(total=Sum('amount'))
    total_revenue = total['total'] or 0
    
    RevenueReport.objects.update_or_create(creators=creator, month=month, year=year, defaults={
      'total_revenue': total_revenue, 'total_subscriptions': total_subscriptions})
    
    CreatorAnalytics.objects.update_or_create(creator=creator, defaults={'total_revenue': total_revenue, 'total_subscriptions': total_subscriptions})
    
    if creator.user.email:
      message = f'{creator.user.username}, total_revenue: {total_revenue}, total_subscriptions: {total_subscriptions}'
      send_mail(
        subject=f'monthly report ({month}/{year})', message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=[creator.user.email], fail_silently=True)

    
      