from courses.models import Lesson, LessonProgress
from django.shortcuts import get_object_or_404
from courses.models import Enrollment
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from engagement.models import Activity
from django.core.cache import cache

def comp_lesson(user, lesson_id):
  lesson = get_object_or_404(Lesson, id=lesson_id)
  course = lesson.section.course
  is_enrolled = Enrollment.objects.filter(user=user, course=course)
  is_enrolled = is_enrolled.exists()
  if user.control != 'subscriber':
    raise PermissionDenied('only stud. allowed')
  progress, created = LessonProgress.objects.get_or_create(user=user, lesson=lesson)
  
  progress.is_completed = True
  progress.completed_at = timezone.now()
  progress.save()
  
  tot_lessons = Lesson.objects.filter(section__course=course)
  tot_lessons = tot_lessons.count()
  comp_lessons = LessonProgress.objects.filter(user=user, lesson__section__course=course, is_completed=True)
  comp_lessons = comp_lessons.count()
  
  if tot_lessons == 0:
      percentage = 0
  else:
      percentage = (comp_lessons / tot_lessons) * 100
  
  Activity.objects.create(user=user, work=f'comp lesson {lesson.title}')
  cache.delete(f'comp{user.id}')
  cache.delete(f'creator_dash{user.id}')
  return {'comp_lesson':True, 'course_prog': round(percentage, 2)}
  