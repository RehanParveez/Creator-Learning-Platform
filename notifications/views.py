from django.shortcuts import render
from rest_framework import viewsets
from notifications.serializers import NotificationSerializer
from notifications.models import Notification

# Create your views here.
class NotificationsViewset(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()