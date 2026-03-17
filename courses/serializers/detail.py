from rest_framework import serializers
from courses.models import Course, Section, Lesson, LessonActivity, Enrollment, LessonProgress, Certificate
from creators.serializers.basic import CreatorProfileSerializer1
from courses.serializers.basic import SectionSerializer1, CourseSerializer1, LessonSerializer1, LessonActivitySerializer1
from engagement.serializers.basic import CommentSerializer1
from accounts.serializers.basic import UserSerializer1

class CourseSerializer(serializers.ModelSerializer):
    creator = CreatorProfileSerializer1(read_only=True)
    sections = SectionSerializer1(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['creator', 'title', 'product', 'description', 'cover', 'price', 'level', 'sections', 'is_premium', 'is_published', 'language', 'lessons', 'students', 'created_at', 'updated_at']
          
class SectionSerializer(serializers.ModelSerializer):
    course = CourseSerializer1(read_only=True)
    lessons = LessonSerializer1(many=True, read_only=True)
    class Meta:
        model = Section
        fields = ['course', 'title', 'description', 'lessons', 'order', 'created_at']
        
class LessonSerializer(serializers.ModelSerializer):
    section = SectionSerializer1(read_only=True)
    activities = LessonActivitySerializer1(many=True, read_only=True)
    comments = CommentSerializer1(many=True, read_only=True)
    class Meta:
        model = Lesson
        fields = ['section', 'title', 'description', 'activities', 'comments', 'video_url', 'duration', 'is_preview', 'order', 'created_at']
            
class LessonActivitySerializer(serializers.ModelSerializer):
    lesson = LessonSerializer1(read_only=True)
    class Meta:
        model = LessonActivity
        fields = ['lesson', 'file', 'uploaded_by', 'created_at']
        
class LessonActivitySerializer1(serializers.ModelSerializer):
    class Meta:
        model = LessonActivity
        fields = ['file', 'created_at']
        
class EnrollmentSerializer(serializers.ModelSerializer):
    user = UserSerializer1(read_only=True)
    course = CourseSerializer1(read_only=True)
    class Meta:
        model = Enrollment
        fields = ['user', 'course', 'enrolled_at', 'is_completed']
        
class LessonProgressSerializer(serializers.ModelSerializer):
    user = UserSerializer1(read_only=True)
    lesson = LessonSerializer1(read_only=True)
    class Meta:
        model = LessonProgress
        fields = ['user', 'lesson', 'is_completed', 'completed_at']
        
class CertificateSerializer(serializers.ModelSerializer):
    user = UserSerializer1(read_only=True)
    course = CourseSerializer1(read_only=True)
    class Meta:
        model = Certificate
        fields = ['user', 'course', 'given_at']