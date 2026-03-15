from django.db import models
from accounts.models import User
from creators.models import CreatorProfile

# Create your models here.
class Course(models.Model):
    DIFFICULTY_CHOICES = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    )
    creator = models.ForeignKey(CreatorProfile, on_delete=models.CASCADE, related_name='created_courses')
    title = models.CharField(max_length=55)
    description = models.TextField()
    cover = models.ImageField(upload_to = 'course_cover/')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    level = models.CharField(max_length=55, choices=DIFFICULTY_CHOICES, default='beginner')
    is_premium = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    language = models.CharField(max_length=55)
    lessons = models.IntegerField(default=0)
    students = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=55)
    description = models.TextField(blank=True)
    order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Lesson(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=55)
    description = models.TextField()
    video_url = models.URLField()
    duration = models.IntegerField()
    is_preview = models.BooleanField(default=False)
    order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class LessonActivity(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='activities')
    file = models.FileField(upload_to = 'lesson_activities/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.created_at)
    
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name = 'enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    
    class Meta:
        constraints = [models.UniqueConstraint(fields = ['user', 'course'], name = 'unique_enrollment')] 
        
    def __str__(self):
        return str(self.enrolled_at)
    
class LessonProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields = ['user', 'lesson'], name = 'unique_progress')]
    
    def __str__(self):
        return str(self.completed_at)
        
class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    given_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.given_at)
    
    
