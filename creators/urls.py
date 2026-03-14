from creators.views import CreatorsViewset
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'creator', CreatorsViewset, basename='creator')

urlpatterns = [
    path('', include(router.urls)),
]