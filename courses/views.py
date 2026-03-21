from django.shortcuts import render
from rest_framework import viewsets
from courses.serializers.detail import CourseSerializer, SectionSerializer, LessonSerializer, LessonActivitySerializer, EnrollmentSerializer, LessonProgressSerializer, CertificateSerializer
from courses.models import Course, Section, Lesson, LessonActivity, Enrollment, LessonProgress, Certificate
from accounts.permissions import CreatorPermission, SubscriberPermission
from rest_framework.decorators import action
from courses.services import comp_lesson
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CourseViewset(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all().order_by('id')
    permission_classes = [CreatorPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['title', 'price']
    ordering_fields = ['created_at']
    filterset_fields = ['title', 'students', 'updated_at', 'created_at']
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      if user.control == 'creator':
        return self.queryset.filter(creator__user=user)

      return self.queryset.none()
    
class SectionViewset(viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    queryset = Section.objects.all().order_by('id')
    permission_classes = [CreatorPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']
    filterset_fields = ['title', 'order', 'created_at']
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      if user.control == 'creator':
        return self.queryset.filter(course__creator__user=user)

      return self.queryset.none()
    
class LessonViewset(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all().order_by('id')
    permission_classes = [CreatorPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']
    filterset_fields = ['title', 'is_preview', 'order', 'created_at']
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      if user.control == 'creator':
        return self.queryset.filter(section__course__creator__user=user)

      return self.queryset.none()
    
class LessonActivityViewset(viewsets.ModelViewSet):
    serializer_class = LessonActivitySerializer
    queryset = LessonActivity.objects.all().order_by('id')
    permission_classes = [CreatorPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['created_at']
    ordering_fields = ['created_at']
    filterset_fields = ['created_at']
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      if user.control == 'creator':
        return self.queryset.filter(lesson__section__course__creator__user=user)
    
      return self.queryset.none()
    
class EnrollmentViewset(viewsets.ModelViewSet):
    serializer_class = EnrollmentSerializer
    queryset = Enrollment.objects.all().order_by('id')
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['enrolled_at']
    ordering_fields = ['enrolled_at']
    filterset_fields = ['is_completed', 'enrolled_at']
    
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
    queryset = LessonProgress.objects.all().order_by('id')
    permission_classes = [SubscriberPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['is_completed']
    ordering_fields = ['completed_at']
    filterset_fields = ['completed_at', 'is_completed']
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      if user.control == 'subscriber':
        return self.queryset.filter(user=user)

      return self.queryset.none()
    
    @action(detail=False, methods=['post'])
    def complete_action(self, request):
        lesson_id = request.data.get('lesson_id')
        lesson = get_object_or_404(Lesson, id=lesson_id)
        res = comp_lesson(user=request.user, lesson=lesson)
        return Response(res, status=200)
    
class CertificateViewset(viewsets.ModelViewSet):
    serializer_class = CertificateSerializer
    queryset = Certificate.objects.all().order_by('id')
    permission_classes = [SubscriberPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['given_at']
    ordering_fields = ['given_at']
    filterset_fields = ['given_at']
    
    def get_queryset(self):
      user = self.request.user

      if user.control == 'platformadmin':
        return self.queryset
      if user.control == 'subscriber':
        return self.queryset.filter(user=user)
      if user.control == 'creator':
        return self.queryset.filter(course__creator__user=user)

      return self.queryset.none()
