from django.shortcuts import render
from rest_framework import viewsets
from creators.serializers.detail import CreatorProfileSerializer
from creators.models import CreatorProfile
from accounts.permissions import CreatorPermission

# Create your views here.
class CreatorsViewset(viewsets.ModelViewSet):
    serializer_class = CreatorProfileSerializer
    queryset = CreatorProfile.objects.all()
    permission_classes = [CreatorPermission]
