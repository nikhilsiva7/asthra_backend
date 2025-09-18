from rest_framework import serializers
from .models import Student,Skill,MentorshipRequest,Internship,InternshipApplication,Training,TrainingEnrollment,Feedback

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class MentorshipRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorshipRequest
        fields = '__all__'

class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        fields = '__all__'        

class InternshipApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternshipApplication
        fields = '__all__'  

class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__' 

class TrainingEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingEnrollment
        fields = '__all__' 

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
