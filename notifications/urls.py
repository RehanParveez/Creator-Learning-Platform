from notifications.views import NotificationsViewset
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'notification', NotificationsViewset, basename='notification')

urlpatterns = [
    path('', include(router.urls)),
]