from analytics.views import AnalyticsViewset, RevenueViewset
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'analytics', AnalyticsViewset, basename='analytics')
router.register(r'revenue', RevenueViewset, basename='revenue')

urlpatterns = [
    path('', include(router.urls)),
]