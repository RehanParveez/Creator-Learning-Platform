from rest_framework import serializers
from engagement.models import Comment

class CommentSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'content', 'created_at']