from rest_framework import serializers
from engagement.models import Comment, Like, Activity

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'lesson', 'content', 'created_at', 'updated_at']
        
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user', 'lesson', 'created_at']
        
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['user', 'work', 'created_at']