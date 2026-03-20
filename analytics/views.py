from django.shortcuts import render
from rest_framework import viewsets
from analytics.serializers import AnalyticsSerializer, RevenueSerializer
from analytics.models import CreatorAnalytics, RevenueReport
from accounts.permissions import CreatorPermission, PlatformAdminPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import action
from subscriptions.models import Subscription
from django.db.models import Count
from courses.models import Course, LessonProgress
from rest_framework.response import Response
from django.db.models import Sum
from django.core.cache import cache

# Create your views here.
class AnalyticsViewset(viewsets.ModelViewSet):
    serializer_class = AnalyticsSerializer
    queryset = CreatorAnalytics.objects.all().order_by('id')
    permission_classes = [CreatorPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['total_courses']
    ordering_fields = ['updated_at']
    filterset_fields = ['total_students', 'total_courses', 'total_views', 'updated_at']
    
    def get_queryset(self):
      user = self.request.user
      
      if user.control == 'creator':
        return self.queryset.filter(creator__user=user)
      return self.queryset
    
    def list(self, request, *args, **kwargs):
     user = request.user
     cache_key = f'creator_dash{user.id}'
     clear = cache.get(cache_key)
     if not clear:
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        clear = serializer.data
        cache.set(cache_key, clear, timeout=60 * 4)
     return Response(clear)
    
    @action(detail=False, methods=['get'])
    def subscrib_inc(self, request):
      user = request.user
      cache_key = f'sub_inc{user.id}'
      clear = cache.get(cache_key)
      if clear:
        return Response(clear)

      subscriptions = Subscription.objects.all()
      if user.control == 'creator':
        subscriptions = subscriptions.filter(plan__product__creator__user=user)
      res = subscriptions.values('started_at__year', 'started_at__month').annotate(total=Count('id')).order_by('started_at__year', 'started_at__month')
      clear = list(res)
      cache.set(cache_key, clear, timeout=60 * 2)
      return Response(clear)
    
    @action(detail=False, methods=['get'])
    def course_comple(self, request):
      user = request.user
      cache_key = f'comp{user.id}'
      clear = cache.get(cache_key)
      if clear:
        return Response(clear)
      
      courses = Course.objects.all()
      if user.control == 'creator':
        courses = courses.filter(product__creator__user=user)

      res = []
      for course in courses:
        total_lessons = course.sections.aggregate(total=Count('lessons'))['total']
        if total_lessons is None:
          total_lessons = 0
          
        completed = LessonProgress.objects.filter(lesson__section__course=course, is_completed=True)
        completed=completed.count()
        if total_lessons == 0:
          percentage = 0
        else:
          percentage = (completed / total_lessons) * 100
        res.append({'course': course.title, 'completion_rate': round(percentage, 2)})
      cache.set(cache_key, res, timeout=60 * 2)
      return Response(res)
    
class RevenueViewset(viewsets.ModelViewSet):
    serializer_class = RevenueSerializer
    queryset = RevenueReport.objects.all().order_by('id')
    permission_classes = [PlatformAdminPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['month']
    ordering_fields = ['created_at']
    filterset_fields = ['month', 'year', 'created_at']
    
    def get_queryset(self):
      user = self.request.user
      
      if user.control == 'creator':
        return self.queryset.filter(creators__user=user)
      return self.queryset
    
    @action(detail=False, methods=['get'])
    def creator_report(self, request):
      user = request.user
      cache_key = f'creator_report{user.id}'
      clear = cache.get(cache_key)
      if clear:
        return Response(clear)
      queryset = self.get_queryset()

      if user.control == 'creator':
        queryset = queryset.filter(creators__user=user)
      res = queryset.values('month', 'year').annotate(total_revenue=Sum('total_revenue'), total_subscriptions=Sum('total_subscriptions')).order_by('year', 'month')
      clear = list(res)
      cache.set(cache_key, clear, timeout=60 * 6)
      return Response(clear)
    