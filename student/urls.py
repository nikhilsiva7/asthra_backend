from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StudentViewSet, SkillViewSet, MentorshipRequestViewSet,
    InternshipViewSet, InternshipApplicationViewSet,
    TrainingViewSet, TrainingEnrollmentViewSet, FeedbackViewSet
)

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'mentorship-requests', MentorshipRequestViewSet)
router.register(r'internships', InternshipViewSet)
router.register(r'internship-applications', InternshipApplicationViewSet)
router.register(r'trainings', TrainingViewSet)
router.register(r'training-enrollments', TrainingEnrollmentViewSet)
router.register(r'feedbacks', FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
