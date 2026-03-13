from django.contrib import admin
from courses.models import Course, Section, Lesson, LessonActivity, Enrollment, LessonProgress, Certificate

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['creator', 'title', 'description', 'cover', 'price', 'level', 'is_premium', 'is_published', 'language', 'lessons', 'students', 'created_at', 'updated_at']
    
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['course', 'title', 'description', 'order', 'created_at']
    
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['section', 'title', 'description', 'video_url', 'duration', 'is_preview', 'order', 'created_at']
    
@admin.register(LessonActivity)
class LessonActivityAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'file', 'uploaded_by', 'created_at']
    
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'enrolled_at', 'is_completed']
    
@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'lesson', 'is_completed', 'completed_at']
    
@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'given_at']