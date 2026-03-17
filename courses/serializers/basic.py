from rest_framework import serializers
from courses.models import Course, Section, Lesson, LessonActivity

class SectionSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['title', 'order']

class CourseSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['title', 'product', 'description', 'price', 'level', 'language']
        
class LessonSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'description', 'duration', 'order']
        
class LessonActivitySerializer1(serializers.ModelSerializer):
    class Meta:
        model = LessonActivity
        fields = ['file', 'created_at']