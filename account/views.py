from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from account.models import CustomUser
from account.serializers import RegisterSerializer, UserSerializer
from alumni.models import Alumni, Skill

from django.db.models import Q

class RegisterAlumniView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Check for existing user with same email or username
        email = request.data.get('email')
        

        if CustomUser.objects.filter(Q(email=email)).exists():
            return Response(
                {'error': 'An account with this email  already exists.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user_serializer = RegisterSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            login(request, user)

            alumni = Alumni.objects.create(
                user=user,
                f_name=request.data['f_name'],
                l_name=request.data['l_name'],
                gender=request.data['gender'],
                passed_year=request.data['passed_year'],
                branch=request.data['branch'],
                job_role=request.data['job_role'],
                experience=request.data['experience'],
                connections=request.data['connections'],
                mobile_number=request.data['mobile_number'],
                linkedin_profile=request.data.get('linkedin_profile'),
                working_company=request.data.get('working_company')
            )

            skill_names = request.data.get('skills', [])
            for name in skill_names:
                skill, _ = Skill.objects.get_or_create(name=name)
                alumni.skills.add(skill)

            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user = authenticate(
            request,
            username=request.data.get('username'),
            password=request.data.get('password')
        )
        if user:
            login(request, user)
            return Response(UserSerializer(user).data)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out successfully'})