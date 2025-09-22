from rest_framework import serializers
from .models import Alumni,JobBoard,Application,Skill,Mentor,Forum,Feedback

class AlumniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumni
        fields = '__all__'

class JobBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobBoard
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'

class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'




class AlumniRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Alumni
        fields = '__all__'

    def create(self, validated_data):
        raw_password = validated_data.pop("password")
        alumni = Alumni(**validated_data)
        alumni.set_password(raw_password)  # hashes password
        return alumni


class AlumniLoginSerializer(serializers.Serializer):
    mobile_number = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            alumni = Alumni.objects.get(email=data["email"])
        except Alumni.DoesNotExist:
            raise serializers.ValidationError("Alumni not found")

        if not alumni.check_password(data["password"]):
            raise serializers.ValidationError("Invalid password")

        return alumni
