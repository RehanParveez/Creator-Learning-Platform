from django.db import models
from accounts.models import User
from courses.models import Lesson

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'comments')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name = 'comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}'
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'likes')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name = 'likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields = ['user', 'lesson'], name = 'unique_like')]

    def __str__(self):
        return f'{self.user} liked {self.lesson}'
    
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'activities')
    work = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.work} by {self.user}'
    

