from accounts.tests import ParentTest
from creators.models import CreatorProfile
from subscriptions.models import Product, Plan, Subscription
from billing.models import PaymentMethod
from django.test import TestCase
from django.contrib.auth import get_user_model
from subscriptions.services import create_sub
from unittest.mock import patch
from django.utils import timezone
from datetime import timedelta
from engagement.models import Activity

# Create your tests here.
class SubscriptionViewsetTest(ParentTest):
  def setUp(self):
    super().setUp()
    self.crea_profile = CreatorProfile.objects.create(user=self.crea_user)
    self.product = Product.objects.create(name = 'product1', creator=self.crea_profile)
    self.plan = Plan.objects.create(product=self.product, name = 'plan1', price=1000, billing = 'monthly')
    self.pay_method = PaymentMethod.objects.create(user=self.sub_user, method_type = 'stripe', is_default=True)
    
  def test_subscrip(self):
        self.authenticate_user('subscriber')
        res = self.client.post('/subscriptions/subscription/', data={'plan_id': self.plan.id, 'pay_method_id': self.pay_method.id})
        self.assertEqual(res.status_code, 201)

class CreateSubServiceTest(TestCase):
  def setUp(self):
    User = get_user_model()
    self.user = User.objects.create_user(username = 'subscriber', email='subscriber@gmail.com', control = 'subscriber')
    self.crea_user = User.objects.create_user(username = 'creator', email='creator@gmail.com', control = 'creator')
    self.crea_profile = CreatorProfile.objects.create(user=self.crea_user)
    self.product = Product.objects.create(name = 'product1', creator=self.crea_profile)
    self.plan = Plan.objects.create(product=self.product, name = 'Plan1', price=900, billing = 'monthly')
    self.pay_method = PaymentMethod.objects.create(user=self.user, method_type = 'stripe', is_default=True)
  
  def test_create_sub(self):
    subscrip = create_sub(user=self.user, plan_id=self.plan.id, pay_method_id=self.pay_method.id)
    self.assertIsInstance(subscrip, Subscription)
    self.assertEqual(subscrip.user, self.user)
    self.assertEqual(subscrip.plan, self.plan)

class SubscriptionSignalTest(TestCase):
  def setUp(self):
    User = get_user_model()
    self.creator = User.objects.create_user(username='creator', email = 'creator@gmail.com')
    self.subscriber = User.objects.create_user(username = 'subscriber', email = 'subscriber@gmail.com')
    self.profile = CreatorProfile.objects.create(user=self.creator)
    self.product = Product.objects.create(name = 'product1', creator=self.profile)
    self.plan = Plan.objects.create(product=self.product, name = 'plan1', price=100, billing = 'monthly')

  @patch('notifications.tasks.notification_email.delay')
  def test_subscrip_signal(self, mock_email):
    started_at = timezone.now()
    expires_at = started_at + timedelta(days=30)
    Subscription.objects.create(user=self.subscriber, plan=self.plan, started_at=started_at, expires_at=expires_at, status = 'active')
    self.assertEqual(Activity.objects.count(), 1)
    self.assertTrue(mock_email.called)
