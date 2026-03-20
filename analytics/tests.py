from accounts.tests import ParentTest
from courses.models import CreatorProfile
from subscriptions.models import Product
from courses.models import Course
from analytics.models import CreatorAnalytics

# Create your tests here.
class AnalyticsViewsetTest(ParentTest):
  def setUp(self):
    super().setUp()
    self.crea_profile = CreatorProfile.objects.create(user=self.crea_user)
    self.product = Product.objects.create(name = 'product2', creator=self.crea_profile, description = 'this is the desc of product2')
    self.course = Course.objects.create(title = 'course2', creator=self.crea_profile, product=self.product, price=800, language = 'urdu')
    CreatorAnalytics.objects.create(creator=self.crea_profile, total_courses=4, total_students=8, total_views=500)
  
  def test_list(self):
    self.authenticate_user('creator')
    res = self.client.get('/analytics/analytics/')
    self.assertEqual(res.status_code, 200)
    self.assertEqual(len(res.data), 1)
  
  def test_subscrib_inc(self):
    self.authenticate_user('creator')
    res = self.client.get('/analytics/analytics/subscrib_inc/')
    self.assertEqual(res.status_code, 200)
  
  def test_course_comple(self):
    self.authenticate_user('creator')
    res = self.client.get('/analytics/analytics/course_comple/')
    self.assertEqual(res.status_code, 200)
    self.assertIn('completion_rate', res.data[0])
