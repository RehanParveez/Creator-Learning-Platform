from rest_framework import serializers
from creators.models import CreatorProfile
from accounts.serializers.basic import UserSerializer1

class CreatorProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer1(read_only=True)
    class Meta:
        model = CreatorProfile
        fields = ['user', 'name', 'bio', 'picture', 'website', 'linkedin_url', 'youtube_url', 'followers', 'courses', 'is_verified', 'created_at', 'updated_at']
        

        