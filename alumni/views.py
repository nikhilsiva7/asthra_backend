from django.shortcuts import render
from .models import Alumni,JobBoard,Application,Skill,Mentor,Forum,Feedback
from .serializers import AlumniSerializer,JobBoardSerializer,ApplicationSerializer,SkillSerializer,MentorSerializer,FeedbackSerializer,ForumSerializer,AlumniLoginSerializer,AlumniRegisterSerializer
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.views import APIView
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

class MentorViewSet(viewsets.ModelViewSet):
    queryset=Mentor.objects.all()
    serializer_class=MentorSerializer

class ForumViewSet(viewsets.ModelViewSet):
    queryset=Forum.objects.all()
    serializer_class=ForumSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset=Feedback.objects.all()
    serializer_class=FeedbackSerializer

class AlumniRegisterView(APIView):
    def post(self, request):
        serializer = AlumniRegisterSerializer(data=request.data)
        if serializer.is_valid():
            alumni = serializer.save()
            return Response({"message": "Registration successful", "id": alumni.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlumniLoginView(APIView):
    def post(self, request):
        serializer = AlumniLoginSerializer(data=request.data)
        if serializer.is_valid():
            alumni = serializer.validated_data
            return Response({
                "message": "Login successful",
                "alumni_id": alumni.id,
                "name": f"{alumni.f_name} {alumni.l_name}",
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)