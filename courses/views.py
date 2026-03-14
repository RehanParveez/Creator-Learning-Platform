from django.shortcuts import render
from rest_framework import viewsets
from courses.serializers.detail import CourseSerializer, SectionSerializer, LessonSerializer, LessonActivitySerializer, EnrollmentSerializer, LessonProgressSerializer, CertificateSerializer
from courses.models import Course, Section, Lesson, LessonActivity, Enrollment, LessonProgress, Certificate
from accounts.permissions import CreatorPermission, SubscriberPermission

# Create your views here.
class CourseViewset(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [CreatorPermission]
    
class SectionViewset(viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = [CreatorPermission]
    
class LessonViewset(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [CreatorPermission]
    
class LessonActivityViewset(viewsets.ModelViewSet):
    serializer_class = LessonActivitySerializer
    queryset = LessonActivity.objects.all()
    permission_classes = [CreatorPermission]
    
class EnrollmentViewset(viewsets.ModelViewSet):
    serializer_class = EnrollmentSerializer
    queryset = Enrollment.objects.all()
    permission_classes = [SubscriberPermission]
    
class LessonProgressViewset(viewsets.ModelViewSet):
    serializer_class = LessonProgressSerializer
    queryset = LessonProgress.objects.all()
    permission_classes = [SubscriberPermission]
    
class CertificateViewset(viewsets.ModelViewSet):
    serializer_class = CertificateSerializer
    queryset = Certificate.objects.all()
    permission_classes = [SubscriberPermission]
