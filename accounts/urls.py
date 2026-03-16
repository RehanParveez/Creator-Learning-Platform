from accounts.views import UserViewset, FollowerViewset
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from accounts.views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'user', UserViewset, basename='user')
router.register(r'follower', FollowerViewset, basename='follower')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view()),
    path('tokenobtain/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('tokenrefresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
