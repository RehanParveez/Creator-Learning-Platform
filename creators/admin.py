from django.contrib import admin
from creators.models import CreatorProfile

# Register your models here.
@admin.register(CreatorProfile)
class CreatorProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'bio', 'picture', 'website', 'linkedin_url', 'youtube_url', 'followers', 'courses', 'is_verified', 'created_at', 'updated_at']
    