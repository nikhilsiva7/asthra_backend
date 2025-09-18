from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('alumni', 'Alumni'),
        ('staff', 'Staff'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    linkedin_username = models.CharField(max_length=100, unique=True, blank=True, null=True)

    def linkedin_url(self):
        if self.linkedin_username:
            return f"https://www.linkedin.com/in/{self.linkedin_username}/"
        return None

    def __str__(self):
        return f"{self.username} - {self.role}"
