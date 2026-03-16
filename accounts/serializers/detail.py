from rest_framework import serializers
from accounts.models import User, Follower

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'phone', 'dob', 'is_creator', 'is_active', 'is_staff', 'date_joined', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        user=User.objects.create_user(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            password=validated_data.get('password'),
            phone=validated_data.get('phone'),
            dob=validated_data.get('dob'),
            is_creator=validated_data.get('is_creator'),
            is_active=validated_data.get('is_active'),
            is_staff=validated_data.get('is_staff'),
            date_joined=validated_data.get('date_joined'),
            created_at=validated_data.get('created_at'),
            updated_at=validated_data.get('updated_at'),  
        )
        return user
        
class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ['follower', 'creator', 'created_at', 'updated_at']
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'control']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user