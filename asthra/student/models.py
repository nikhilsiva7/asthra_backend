from django.db import models
from alumni.models import Mentor

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    year=models.IntegerField(max_length=4)
    skills=models.ManyToManyField('Skill',blank=True)
    def __str__(self):
        return self.name

class Skill(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class MentorshipRequest(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    mentor=models.ForeignKey(Mentor,on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected")
    ], default="pending")
    def __str__(self):
        return self.student.name

class Internship(models.Model):
    title=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    description=models.TextField()
    skills_required=models.ManyToManyField('Skill',blank=True)
    posted_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title} at {self.company}"

class InternshipApplication(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    internship=models.ForeignKey(Internship,on_delete=models.CASCADE)
    applied_at=models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected")
    ], default="pending")
    def __str__(self):
        return f"{self.student.name} applied for {self.internship.title}"
    
class Training(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    duration_weeks=models.IntegerField()
    skills_covered=models.ManyToManyField('Skill')
    def __str__(self):
        return self.title

class TrainingEnrollment(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    training=models.ForeignKey(Training,on_delete=models.CASCADE)
    enrolled_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.student.name} enrolled in {self.training.title}"

class Feedback(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    category=models.CharField(max_length=10,choices=[
         ("mentorship", "Mentorship"),
        ("internship", "Internship"),
        ("webinar", "Webinar"),
        ("training", "Training"),
    ])
    description=models.TextField()
    rating=models.IntegerField(choices=[
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ])
    def __str__(self):
        return f"{self.student.name} gave feedback for {self.category}"
    

    
