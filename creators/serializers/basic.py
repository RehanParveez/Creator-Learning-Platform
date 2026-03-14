from rest_framework import serializers
from creators.models import CreatorProfile
from accounts.serializers.basic import UserSerializer1

class CreatorProfileSerializer1(serializers.ModelSerializer):
    user = UserSerializer1(read_only=True)
    class Meta:
        model = CreatorProfile
        fields = ['user', 'name', 'bio', 'picture', 'website', 'followers']