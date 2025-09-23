from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from account.models import CustomUser
from account.serializers import RegisterSerializer, UserSerializer
from alumni.models import Alumni, Skill
from django.contrib.auth import get_user_model
class RegisterAlumniView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data

        # Validate required fields
        required_fields = ['college_Id', 'college_Email', 'name', 'password', 'graduationYear', 'branch']
        missing = [field for field in required_fields if not data.get(field)]
        if missing:
            return Response({'error': f'Missing fields: {", ".join(missing)}'}, status=status.HTTP_400_BAD_REQUEST)

        # Check for duplicates
        if CustomUser.objects.filter(username=data['college_Id']).exists():
            return Response({'error': 'College ID already registered'}, status=status.HTTP_400_BAD_REQUEST)
        if CustomUser.objects.filter(email=data['college_Email']).exists():
            return Response({'error': 'Email already registered'}, status=status.HTTP_400_BAD_REQUEST)

        # Split name safely
        name_parts = data['name'].strip().split()
        first_name = name_parts[0]
        last_name = " ".join(name_parts[1:]) if len(name_parts) > 1 else ""

        # Create user
        user = CustomUser.objects.create_user(
            username=data['college_Id'],
            email=data['college_Email'],
            password=data['password'],
            first_name=first_name,
            last_name=last_name,
            role='alumni'
        )
        login(request, user)

        # Create alumni profile
        alumni = Alumni.objects.create(
            user=user,
            name=data['name'],
            passed_year=int(data['graduationYear']),
            branch=data['branch'],
            job_role=data.get('jobTitle', ''),
            experience=0,
            connections=0,
            mobile_number="+919999999999",  # TODO: make dynamic
            linkedin_profile="",
            working_company=data.get('currentCompany', '')
        )

        # Add skills if provided
        skill_names = data.get('skills', [])
        for name in skill_names:
            skill, _ = Skill.objects.get_or_create(name=name)
            alumni.skills.add(skill)

        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user_obj = get_user_model().objects.get(email=email)
        except get_user_model().DoesNotExist:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

        user = authenticate(request, username=user_obj.username, password=password)
        if user:
            login(request, user)
            return Response(UserSerializer(user).data)
        return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out successfully'})