from django.shortcuts import render
from .models import Alumni,JobBoard,Application,Skill
from .serializers import AlumniSerializer,JobBoardSerializer,ApplicationSerializer,SkillSerializer
from rest_framework import viewsets
# Create your views here.

class AlumniViewSet(viewsets.ModelViewSet):
    queryset = Alumni.objects.all()
    serializer_class = AlumniSerializer

class JobBoardViewSet(viewsets.ModelViewSet):
    queryset = JobBoard.objects.all()
    serializer_class = JobBoardSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset=Skill.objects.all()
    serializer_class=SkillSerializer

