from accounts.tests import ParentTest
from creators.models import CreatorProfile
from subscriptions.models import Product
from courses.models import Course, Section, Lesson, Enrollment
from django.test import TestCase
from django.contrib.auth import get_user_model
from courses.services import comp_lesson
from django.core.exceptions import PermissionDenied
from subscriptions.models import Plan
from subscriptions.models import Subscription
from django.utils import timezone
from datetime import timedelta
from unittest.mock import patch
from engagement.models import Activity

# Create your tests here.
class CourseViewsetTest(ParentTest):
  def setUp(self):
    super().setUp()
    self.creator_prof = CreatorProfile.objects.create(user=self.crea_user)
    self.product = Product.objects.create(name = 'product1', creator=self.creator_prof, description = 'this is the des of product1')
    self.course = Course.objects.create(title = 'course1', creator=self.creator_prof, product=self.product, price=1000, language = 'urdu')
    
  def test_course_allowed(self):
    self.authenticate_user('creator')
    res = self.client.get('/courses/course/')
    self.assertEqual(res.status_code, 200)
    if 'results' in res.data:
      courses = res.data['results']
    else:
      courses = res.data
    check = []
    for course in courses:
      if course['title'] == 'course1':
        check.append(course)
    self.assertTrue(len(check) > 0)
  
  def test_course_denied(self):
    self.authenticate_user('subscriber')
    res = self.client.get('/courses/course/')
    self.assertEqual(res.status_code, 403)

class CompLessonServiceTest(TestCase):
  def setUp(self):
    User = get_user_model()
    self.sub_user = User.objects.create_user(username = 'subscriber', email='subscriber@gmail.com', control = 'subscriber')
    self.crea_user = User.objects.create_user(username = 'creator', email='creator@gmail.com', control = 'creator')
    self.crea_profile = CreatorProfile.objects.create(user=self.crea_user)
    self.product = Product.objects.create(name = 'product2', creator=self.crea_profile, description = 'this des is of product2')
    self.course = Course.objects.create(title = 'course1', creator=self.crea_profile, product=self.product, price=1000, language = 'hindi')
    self.section = Section.objects.create(course=self.course, title = 'section1', order=1)
    self.lesson = Lesson.objects.create(title = 'lesson1', section=self.section, duration=25, order=1)
    Enrollment.objects.create(user=self.sub_user, course=self.course)
  
  def test_comp_lesson(self):
    res = comp_lesson(user=self.sub_user, lesson_id=self.lesson.id)
    self.assertTrue(res['comp_lesson'])
    self.assertIn('course_prog', res)

  def test_denied(self):
        with self.assertRaises(PermissionDenied):
            comp_lesson(user=self.crea_user, lesson_id=self.lesson.id)

class LessonSignalTest(TestCase):
  def setUp(self):
    User = get_user_model()
    self.creator = User.objects.create_user(username='creator', email = 'course@gmail.com')
    self.subscriber = User.objects.create_user(username= 'subscriber', email = 'subscriber@gmail.com')
    self.profile = CreatorProfile.objects.create(user=self.creator)
    self.product = Product.objects.create(name = 'product1', creator=self.profile)
    self.plan = Plan.objects.create(product=self.product, name = 'plan1', price=1000, billing = 'monthly')
    started_at = timezone.now()
    expires_at = started_at + timedelta(days=30)
    Subscription.objects.create(user=self.subscriber, plan=self.plan, started_at=started_at, expires_at=expires_at, status='active')
    self.course = Course.objects.create(title = 'course1', creator=self.profile, product=self.product, price=800, language = 'urdu')
    self.section = Section.objects.create(course=self.course, title = 'section1', order=1)

  @patch('notifications.tasks.notification_email.delay')
  def test_less_signal(self, mock_email):
    Activity.objects.all().delete()
    Lesson.objects.create(section=self.section, title = 'lesson2', description = 'this is the desc of lesson2', video_url= 'http://url.com', duration=25, order=1, is_preview=False)
    self.assertEqual(Activity.objects.count(), 1)
    self.assertTrue(mock_email.called)

  @patch('notifications.tasks.notification_email.delay')
  def test_preview_lessl(self, mock_email):
    Activity.objects.all().delete()
    Lesson.objects.create(section=self.section, title = 'lesson3', description = 'this is the desc of lesson3', video_url = 'http://url.com', duration=27, order=2, is_preview=True)
    self.assertEqual(Activity.objects.count(), 0)
    self.assertFalse(mock_email.called)
                    
class CourseSignalTest(TestCase):
  def setUp(self):
    User = get_user_model()
    self.user = User.objects.create_user(username = 'creator', email = 'course@gmail.com')
    self.profile = CreatorProfile.objects.create(user=self.user)
    self.product = Product.objects.create(name = 'product1', creator=self.profile)

  def test_course_signal(self):
    Course.objects.create(title = 'course1', creator=self.profile, product=self.product, price=1000, language = 'urdu')
    activities = Activity.objects.all()
    self.assertEqual(len(activities), 1)
            
class LessonViewsetTest(ParentTest):
  def setUp(self):
    super().setUp()
    self.crea_profile = CreatorProfile.objects.create(user=self.crea_user)
    self.product = Product.objects.create(name = 'product1', creator=self.crea_profile)
    self.course = Course.objects.create(title = 'course1', creator=self.crea_profile, product=self.product, price=800, language = 'hindi')
    self.section = Section.objects.create(course=self.course, title = 'section1', order=1)
    self.lesson = Lesson.objects.create(section=self.section, title = 'lesson1', description = 'this is the desc for lesson1', video_url = 'http://lesson.com', duration=30, order=1)

  def test_lessallowed(self):
      self.authenticate_user('creator')
      res = self.client.get('/courses/lesson/')
      self.assertEqual(res.status_code, 200)
      if 'results' in res.data:
        lessons = res.data['results']
      else:
        lessons = res.data
      pre = False
      for lesson in lessons:
        if lesson['title'] == 'lesson1':
          pre = True
          break
      self.assertTrue(pre)
    
class EnrollmentViewsetTest(ParentTest):
  def setUp(self):
    super().setUp()
    self.crea_profile = CreatorProfile.objects.create(user=self.crea_user)
    self.product = Product.objects.create(name = 'product1', creator=self.crea_profile)
    self.course = Course.objects.create(title = 'course1', creator=self.crea_profile, product=self.product, price=1500, language='urdu')
    self.enrollment = Enrollment.objects.create(user=self.sub_user, course=self.course)

  def test_subenroll(self):
    self.authenticate_user('subscriber')
    res = self.client.get('/courses/enrollment/')
    self.assertEqual(res.status_code, 200)
    if 'results' in res.data:
      enrollments = res.data['results']
    else:
      enrollments = res.data
    self.assertTrue(len(enrollments) > 0)

  def test_creaenroll(self):
    self.authenticate_user('creator')
    res = self.client.get('/courses/enrollment/')
    self.assertEqual(res.status_code, 200)
    if 'results' in res.data:
      enrollments = res.data['results']
    else:
      enrollments = res.data
    print('enrolls:', enrollments)
    print('cour id:', self.course.id)
    pre = False
    for enroll in enrollments:
      if enroll['course']['id'] == self.course.id:
         pre = True
         break
    self.assertTrue(pre)