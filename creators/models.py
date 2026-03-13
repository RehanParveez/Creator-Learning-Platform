from django.db import models

# Create your models here.
class CreatorProfile(models.Model):
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE, related_name = 'creator_profile')
    name = models.CharField(max_length=45)
    bio = models.TextField(blank=True)
    picture = models.ImageField(upload_to = 'creator_profiles/', blank=True, null=True)
    website = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    followers = models.IntegerField(default=0)
    courses = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
    
