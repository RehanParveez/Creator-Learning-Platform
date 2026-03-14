from courses.views import CourseViewset, SectionViewset, LessonViewset, LessonActivityViewset, EnrollmentViewset, LessonProgressViewset, CertificateViewset
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'course', CourseViewset, basename='course')
router.register(r'section', SectionViewset, basename='section')
router.register(r'lesson', LessonViewset, basename='lesson')
router.register(r'lessonactivity', LessonActivityViewset, basename='lessonactivity')
router.register(r'enrollment', EnrollmentViewset, basename='enrollment')
router.register(r'lessonprogress', LessonProgressViewset, basename='lessonprogress')
router.register(r'certificate', CertificateViewset, basename='certificate')

urlpatterns = [
    path('', include(router.urls)),
]