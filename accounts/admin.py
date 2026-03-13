from django.contrib import admin
from accounts.models import User, Follower

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone', 'dob', 'is_creator', 'is_active', 'is_staff', 'date_joined', 'created_at', 'updated_at']
    
@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ['follower', 'creator', 'created_at', 'updated_at']
    
