from django.shortcuts import render
from rest_framework import viewsets
from notifications.serializers import NotificationSerializer
from notifications.models import Notification
from accounts.permissions import SubscriberPermission

# Create your views here.
class NotificationsViewset(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    permission_classes = [SubscriberPermission]
    
    from django.shortcuts import render
from rest_framework import viewsets
from notifications.serializers import NotificationSerializer
from notifications.models import Notification
from accounts.permissions import SubscriberPermission

# Create your views here.
class NotificationsViewset(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    permission_classes = [SubscriberPermission]
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      return self.queryset.filter(user=user)