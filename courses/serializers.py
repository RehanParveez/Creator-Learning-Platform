from rest_framework import serializers
from courses.models import Course, Section, Lesson, LessonActivity, Enrollment, LessonProgress, Certificate

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['creator', 'title', 'description', 'cover', 'price', 'level', 'is_premium', 'is_published', 'language', 'lessons', 'students', 'created_at', 'updated_at']
        
class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['course', 'title', 'description', 'order', 'created_at']
        
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['section', 'title', 'description', 'video_url', 'duration', 'is_preview', 'order', 'created_at']
        
class LessonActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonActivity
        fields = ['lesson', 'file', 'uploaded_by', 'created_at']
        
class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['user', 'course', 'enrolled_at', 'is_completed']
        
class LessonProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonProgress
        fields = ['user', 'lesson', 'is_completed', 'completed_at']
        
class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['user', 'course', 'given_at']