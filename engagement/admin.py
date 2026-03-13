from django.contrib import admin
from engagement.models import Comment, Like, Activity

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'lesson', 'content', 'created_at', 'updated_at']
    
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'lesson', 'created_at']
    
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user', 'work', 'created_at']