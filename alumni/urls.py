from django.urls import path,include
from .views import AlumniViewSet,JobBoardViewSet,ApplicationViewSet,SkillViewSet,MentorViewSet
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'alumni', AlumniViewSet)
router.register(r'jobs', JobBoardViewSet)
router.register(r'applications', ApplicationViewSet)
router.register(r'skill', SkillViewSet)
router.register(r'mentor', MentorViewSet)


urlpatterns = [
    path('',include(router.urls)),
]

