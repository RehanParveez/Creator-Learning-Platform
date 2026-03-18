from courses.models import Lesson, LessonProgress
from django.utils import timezone
from engagement.models import Activity

def comp_lesson(user, lesson_id):
  lesson = Lesson.objects.get(id=lesson_id)
  progress, created = LessonProgress.objects.get_or_create(user=user, lesson=lesson)
  progress.is_completed = True
  progress.completed_at = timezone.now()
  progress.save()
  
  course = lesson.section.course
  tot_lessons = Lesson.objects.filter(section__course=course)
  tot_lessons = tot_lessons.count()
  comp_lessons = LessonProgress.objects.filter(user=user, lesson__section__course=course, is_completed=True)
  comp_lessons = comp_lessons.count()
  
  if tot_lessons == 0:
      percentage = 0
  else:
      percentage = (comp_lessons / tot_lessons) * 100
  
  Activity.objects.create(user=user, work=f'comp lesson {lesson.title}')
  return {'comp_lesson':True, 'course_prog': round(percentage, 2)}
  