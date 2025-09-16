from django.urls import path,include
from .views import AlumniViewSet,JobBoardViewSet,ApplicationViewSet,SkillViewSet
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'alumni', AlumniViewSet)
router.register(r'jobs', JobBoardViewSet)
router.register(r'applications', ApplicationViewSet)
router.register(r'skill', SkillViewSet)


urlpatterns = [
    path('',include(router.urls)),
]