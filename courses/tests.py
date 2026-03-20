from accounts.tests import ParentTest
from creators.models import CreatorProfile
from subscriptions.models import Product
from courses.models import Course

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
    
    