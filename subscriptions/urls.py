from subscriptions.views import ProductViewset, PlanViewset, SubscriptionViewset, CouponViewset
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'product', ProductViewset, basename='product')
router.register(r'plan', PlanViewset, basename='plan')
router.register(r'subscription', SubscriptionViewset, basename='subscription')
router.register(r'count', CouponViewset, basename='count')

urlpatterns = [
    path('', include(router.urls)),
]