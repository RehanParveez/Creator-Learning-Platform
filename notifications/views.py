from django.shortcuts import render
from rest_framework import viewsets
from notifications.serializers import NotificationSerializer
from notifications.models import Notification
from accounts.permissions import SubscriberPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.
class NotificationsViewset(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    permission_classes = [SubscriberPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['title', 'message']
    ordering_fields = ['created_at']
    filterset_fields = ['title', 'is_read', 'created_at']
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      return self.queryset.filter(user=user)