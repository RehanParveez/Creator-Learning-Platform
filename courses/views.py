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
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      if user.control == 'creator':
        return self.queryset.filter(creator__user=user)

      return self.queryset.none()
    
class SectionViewset(viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = [CreatorPermission]
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      if user.control == 'creator':
        return self.queryset.filter(course__creator__user=user)

      return self.queryset.none()
    
class LessonViewset(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [CreatorPermission]
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      if user.control == 'creator':
        return self.queryset.filter(section__course__creator__user=user)

      return self.queryset.none()
    
class LessonActivityViewset(viewsets.ModelViewSet):
    serializer_class = LessonActivitySerializer
    queryset = LessonActivity.objects.all()
    permission_classes = [CreatorPermission]
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      if user.control == 'creator':
        return self.queryset.filter(lesson__section__course__creator__user=user)
    
      return self.queryset.none()
    
class EnrollmentViewset(viewsets.ModelViewSet):
    serializer_class = EnrollmentSerializer
    queryset = Enrollment.objects.all()
    permission_classes = [SubscriberPermission]
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      if user.control == 'subscriber':
        return self.queryset.filter(user=user)
      if user.control == 'creator':
        return self.queryset.filter(course__creator__user=user)

      return self.queryset.none()
    
class LessonProgressViewset(viewsets.ModelViewSet):
    serializer_class = LessonProgressSerializer
    queryset = LessonProgress.objects.all()
    permission_classes = [SubscriberPermission]
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      if user.control == 'subscriber':
        return self.queryset.filter(user=user)

      return self.queryset.none()
    
class CertificateViewset(viewsets.ModelViewSet):
    serializer_class = CertificateSerializer
    queryset = Certificate.objects.all()
    permission_classes = [SubscriberPermission]
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      if user.control == 'subscriber':
        return self.queryset.filter(user=user)
      if user.control == 'creator':
        return self.queryset.filter(course__creator__user=user)

      return self.queryset.none()
