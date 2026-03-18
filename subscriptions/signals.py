from django.dispatch import receiver
from django.db.models.signals import post_save
from subscriptions.models import Subscription
from notifications.tasks import notification_email 
from engagement.models import Activity

@receiver(post_save, sender=Subscription)
def notify_subscription(sender, instance, created, **kwargs):
    print('subscription signal check')
    if not created:
      return
    creator = instance.plan.product.creator.user
    notification_email.delay(user_id=creator.id, title = f'subscriber {instance.plan.name}', message = f'{instance.user.username} subscribed {instance.plan.name}')
    Activity.objects.create(user=instance.user, work=f'subscribed {instance.plan.name}')
        