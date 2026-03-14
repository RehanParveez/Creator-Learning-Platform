from django.shortcuts import render
from rest_framework import viewsets
from creators.serializers import CreatorProfileSerializer
from creators.models import CreatorProfile

# Create your views here.
class CreatorsViewset(viewsets.ModelViewSet):
    serializer_class = CreatorProfileSerializer
    queryset = CreatorProfile.objects.all()
