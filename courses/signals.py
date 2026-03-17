from django.dispatch import receiver
from django.db.models.signals import post_save
from courses.models import Lesson
from subscriptions.models import Subscription
from notifications.tasks import notification_email  

@receiver(post_save, sender=Lesson)
def notify_publish(sender, instance, created, **kwargs):
    print('lesson signal check')
    if not created:
      return
    if instance.is_preview: 
      return
    course = instance.section.course
    product = course.product
    if not product:
        return
    plans = product.plans.all()  
    if not plans.exists():
        return
    subscriptions = Subscription.objects.filter(plan__in=plans, status = 'active')
    for sub in subscriptions:
      notification_email.delay(user_id=sub.user.id, title=f'lesson {course.title}', message=f'{instance.title} added to {course.title}')
        