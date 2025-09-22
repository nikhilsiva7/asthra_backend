from django.shortcuts import render
from .models import Alumni,JobBoard,Application,Skill,Mentor,Forum,Feedback
from .serializers import AlumniSerializer,JobBoardSerializer,ApplicationSerializer,SkillSerializer,MentorSerializer,FeedbackSerializer,ForumSerializer,AlumniLoginSerializer,AlumniRegisterSerializer
from rest_framework import viewsets,status,permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login,logout
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
    permission_classes = [permissions.AllowAny]  # allow signup without login

    def post(self, request):
        serializer = AlumniRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)  # 🔑 start session
            return Response(
                {
                    "message": "User registered & logged in successfully",
                    "username": user.username,
                    "role": user.role,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlumniLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = AlumniLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            login(request, user)  # 🔑 start session
            return Response(
                {
                    "message": "Login successful",
                    "username": user.username,
                    "role": user.role,
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlumniLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)