from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password,check_password

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Mentor(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    experience = models.IntegerField()
    mentees = models.IntegerField()
    skills = models.ManyToManyField(Skill, related_name="mentors")

    def __str__(self):
        return self.name


class Alumni(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    passed_year = models.IntegerField()
    branch=models.CharField()
    job_role = models.CharField(max_length=100)
    skills = models.ManyToManyField(Skill, related_name="alumni")
    experience = models.IntegerField()
    connections = models.IntegerField()
    password=models.CharField(max_length=100)

    mobile_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[RegexValidator(r'^\+?\d{10,15}$', "Enter a valid mobile number")]
    )
    linkedin_profile = models.URLField(max_length=200, blank=True, null=True)
    working_company = models.CharField(max_length=100, blank=True, null=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"


class Forum(models.Model):
    alumni = models.ForeignKey(Alumni, on_delete=models.CASCADE, related_name="forums")
    content = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.content[:50]  # First 50 chars only


class Feedback(models.Model):
    category_choices = [
    ('GENERAL', 'General Feedback'),
    ('WEBSITE', 'Website Improvement'),
    ('EVENT', 'Event Suggestions'),
    ('ISSUE', 'Any Issues'),
    ('OTHER', 'Other'), 
    ]

    subject=models.TextField(max_length=500)
    category=models.CharField(choices=category_choices)
    message=models.TextField(max_length=500)

class JobBoard(models.Model):
    job_title=models.CharField(max_length=100)
    job_location=models.CharField(max_length=100)
    skills_required=models.ManyToManyField(Skill,related_name='JobBoard')
    description=models.TextField(max_length=500)
    date_posted=models.DateField(auto_now_add=True)
    job_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    alumni_id=models.ForeignKey(Alumni,on_delete=models.CASCADE)
    app_url=models.URLField()

class Application(models.Model):
    alumni_id=models.ForeignKey(Alumni,on_delete=models.CASCADE)
    job_id=models.ForeignKey(JobBoard,on_delete=models.CASCADE)
    status=models.CharField(max_length=100)


class SuccessStory(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=500)
    alumni_id=models.ForeignKey(Alumni,on_delete=models.CASCADE)
