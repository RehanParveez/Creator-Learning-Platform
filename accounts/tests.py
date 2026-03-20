from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from django.test import TestCase
from creators.models import CreatorProfile
from subscriptions.models import Product
from courses.models import Course
from accounts.permissions import PlatformAdminPermission, CreatorPermission, SubscriberPermission
from types import SimpleNamespace

class ParentTest(APITestCase):
  def setUp(self):
    self.client = APIClient()
    User = get_user_model()
    self.plat_admin = User.objects.create_user(username = 'platformadmin', email = 'platformadmin@gmail.com', control = 'platformadmin', password = 'adm12312')
    self.crea_user = User.objects.create_user(username = 'creator', email = 'creator@gmail.com', control = 'creator', password = 'crea12312')
    self.sub_user = User.objects.create_user(username = 'subscriber', email = 'subscriber@gmail.com', control = 'subscriber', password = 'sub12312')

  def authenticate_user(self, role = 'subscriber'):
    if role == 'platformadmin':
      self.client.force_authenticate(user=self.plat_admin)
      return self.plat_admin
    elif role == 'creator':
      self.client.force_authenticate(user=self.crea_user)
      return self.crea_user
    else:
      self.client.force_authenticate(user=self.sub_user)
      return self.sub_user
        
class CheckTest(ParentTest):
  def test_check(self):
    self.assertEqual(self.plat_admin.username, 'platformadmin')
    self.assertEqual(self.crea_user.username, 'creator')
    self.assertEqual(self.sub_user.username, 'subscriber')
       
class PermissionsTets(TestCase):
  def setUp(self):
    User = get_user_model()
    self.plat_admin = User.objects.create_user(username = 'platformadmin', email = 'platformadmin@gmail.com', control = 'platformadmin', password = 'adm12312')
    self.crea_user = User.objects.create_user(username = 'creator', email = 'creator@gmail.com', control = 'creator', password = 'crea12312')
    self.sub_user = User.objects.create_user(username = 'subscriber', email = 'subscriber@gmail.com', control = 'subscriber', password = 'sub12312')
    
    self.creator_prof = CreatorProfile.objects.create(user=self.crea_user)
    self.product = Product.objects.create(name = 'product1', creator=self.creator_prof, description = 'this is the description of product1')
    self.course = Course.objects.create(title = 'course1', creator=self.creator_prof, product=self.product, price=900, language = 'hindi')
 
  def test_platadmin(self):
    permission = PlatformAdminPermission()
    request = SimpleNamespace(user=self.plat_admin)
    self.assertTrue(permission.has_permission(request, None))
    self.assertTrue(permission.has_object_permission(request, None, self.course))
  
  def test_creator(self):
    permission = CreatorPermission()
    request = SimpleNamespace(user=self.crea_user)
    self.assertTrue(permission.has_permission(request, None))
    self.assertTrue(permission.has_object_permission(request, None, self.course))
  
  def test_creadenied(self):
    permission = CreatorPermission()
    request = SimpleNamespace(user=self.sub_user)
    self.assertFalse(permission.has_permission(request, None))
    self.assertFalse(permission.has_object_permission(request, None, self.course))
  
  def test_subscriber(self):
    permission = SubscriberPermission()
    request = SimpleNamespace(user=self.sub_user)
    self.assertTrue(permission.has_permission(request, None))
    self.assertTrue(permission.has_object_permission(request, None, self.course))
    
 
        
