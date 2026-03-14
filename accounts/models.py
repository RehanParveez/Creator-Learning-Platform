from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    CONTROL_CHOICES = (
        ('platformadmin', 'PlatformAdmin'),
        ('creator', 'Creator'),
        ('subscriber', 'Subscriber'),
        ('user', 'User'),
    )
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    dob = models.DateField(null=True, blank=True)
    is_creator = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    control = models.CharField(max_length=45, choices=CONTROL_CHOICES, default='user')
    date_joined = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email
    
class Follower(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'following')
    creator = models.ForeignKey('creators.CreatorProfile', on_delete=models.CASCADE, related_name = 'creator_followers')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        constraints = [models.UniqueConstraint(fields = ['follower', 'creator'], name = 'unique_follower_creator')]
    
    def __str__(self):
        return f'{self.follower} follows {self.creator}'
        
