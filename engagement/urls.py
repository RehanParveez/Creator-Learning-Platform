from engagement.views import CommentViewset, LikeViewset, ActivityViewset
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'comment', CommentViewset, basename='comment')
router.register(r'like', LikeViewset, basename='like')
router.register(r'activity', ActivityViewset, basename='activity')

urlpatterns = [
    path('', include(router.urls)),
]