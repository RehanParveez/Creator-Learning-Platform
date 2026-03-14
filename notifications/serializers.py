from rest_framework import serializers
from notifications.models import Notification
from accounts.serializers.basic import UserSerializer1

class NotificationSerializer(serializers.ModelSerializer):
    user = UserSerializer1(read_only=True)
    class Meta:
        model = Notification
        fields = ['user', 'title', 'message', 'is_read', 'created_at']
        
