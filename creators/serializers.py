from rest_framework import serializers
from creators.models import CreatorProfile

class CreatorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreatorProfile
        fields = ['user', 'name', 'bio', 'picture', 'website', 'linkedin_url', 'youtube_url', 'followers', 'courses', 'is_verified', 'created_at', 'updated_at']
        
