from django.shortcuts import render
from rest_framework import viewsets
from engagement.serializers import CommentSerializer, LikeSerializer, Activity
from engagement.models import Comment, Like, Activity

# Create your views here.
class CommentViewset(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    
class LikeViewset(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    
class ActivityViewset(viewsets.ModelViewSet):
    serializer_class = Activity
    queryset = Activity.objects.all()