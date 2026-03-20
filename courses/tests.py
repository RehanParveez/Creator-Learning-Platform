from accounts.tests import ParentTest
from creators.models import CreatorProfile
from subscriptions.models import Product
from courses.models import Course, Section, Lesson, Enrollment
from django.test import TestCase
from django.contrib.auth import get_user_model
from courses.services import comp_lesson
from django.core.exceptions import PermissionDenied

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

    