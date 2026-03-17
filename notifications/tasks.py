from celery import shared_task
from accounts.models import User
from notifications.models import Notification
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def notification_email(user_id, title, message):
    user = User.objects.filter(id=user_id).first()
    if not user:
        return  
    Notification.objects.create(user=user, title=title, message=message)
    send_mail(subject=title, message=message, from_email = settings.EMAIL_HOST_USER, recipient_list = [user.email], fail_silently=False)