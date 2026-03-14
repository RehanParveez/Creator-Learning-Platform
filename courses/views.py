from django.shortcuts import render
from rest_framework import viewsets
from courses.serializers import CourseSerializer, SectionSerializer, LessonSerializer, LessonActivitySerializer, EnrollmentSerializer, LessonProgressSerializer, CertificateSerializer
from courses.models import Course, Section, Lesson, LessonActivity, Enrollment, LessonProgress, Certificate

# Create your views here.
class CourseViewset(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    
class SectionViewset(viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    
class LessonViewset(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    
class LessonActivityViewset(viewsets.ModelViewSet):
    serializer_class = LessonActivitySerializer
    queryset = LessonActivity.objects.all()
    
class EnrollmentViewset(viewsets.ModelViewSet):
    serializer_class = EnrollmentSerializer
    queryset = Enrollment.objects.all()
    
class LessonProgressViewset(viewsets.ModelViewSet):
    serializer_class = LessonProgressSerializer
    queryset = LessonActivity.objects.all()
    
class CertificateViewset(viewsets.ModelViewSet):
    serializer_class = CertificateSerializer
    queryset = Certificate.objects.all()
