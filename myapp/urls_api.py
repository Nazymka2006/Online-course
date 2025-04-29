from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import *

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'homeworks', HomeworkViewSet)
router.register(r'submissions', HomeworkSubmissionViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = router.urls  # ← просто это

