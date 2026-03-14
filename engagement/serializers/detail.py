from rest_framework import serializers
from engagement.models import Comment, Like, Activity
from accounts.serializers.basic import UserSerializer1
from courses.serializers.basic import LessonSerializer1
     
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer1(read_only=True)
    lesson = LessonSerializer1(read_only=True)
    class Meta:
        model = Comment
        fields = ['user', 'lesson', 'content', 'created_at', 'updated_at']
          
class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer1(read_only=True)
    lesson = LessonSerializer1(read_only=True)
    class Meta:
        model = Like
        fields = ['user', 'lesson', 'created_at']
        
class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer1(read_only=True)
    class Meta:
        model = Activity
        fields = ['user', 'work', 'created_at']