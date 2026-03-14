from accounts.views import UserViewset, FollowerViewset
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'user', UserViewset, basename='user')
router.register(r'follower', FollowerViewset, basename='follower')

urlpatterns = [
    path('', include(router.urls)),
]
