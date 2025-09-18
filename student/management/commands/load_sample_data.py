from django.core.management.base import BaseCommand
from alumni.models import Skill as AlumniSkill, Mentor, Alumni, Forum, Feedback as AlumniFeedback, JobBoard, Application
from student.models import Student, Skill, MentorshipRequest, Internship, InternshipApplication, Training, TrainingEnrollment, Feedback as StudentFeedback
from django.utils import timezone

class Command(BaseCommand):
    help = 'Load sample data for all apps'

    def handle(self, *args, **options):
        # --- Alumni App Sample Data ---
        alumni_skill_python = AlumniSkill.objects.create(name='Python')
        alumni_skill_communication = AlumniSkill.objects.create(name='Communication')
        alumni_skill_leadership = AlumniSkill.objects.create(name='Leadership')

        mentor1 = Mentor.objects.create(name='Dr. John', profession='Engineer', experience=12, mentees=8)
        mentor1.skills.add(alumni_skill_python, alumni_skill_leadership)

        alumni1 = Alumni.objects.create(
            f_name='Jane', l_name='Doe', gender='F', passed_year=2020, job_role='Developer',
            experience=3, connections=50, mobile_number='+911234567890', linkedin_profile='https://linkedin.com/in/janedoe', working_company='TechCorp'
        )
        alumni1.skills.add(alumni_skill_python, alumni_skill_communication)

        alumni2 = Alumni.objects.create(
            f_name='Mike', l_name='Smith', gender='M', passed_year=2019, job_role='Manager',
            experience=5, connections=100, mobile_number='+919876543210', linkedin_profile='https://linkedin.com/in/mikesmith', working_company='BizInc'
        )
        alumni2.skills.add(alumni_skill_leadership)

        Forum.objects.create(alumni=alumni1, content='Welcome to the alumni forum!', likes=10, dislikes=0)
        Forum.objects.create(alumni=alumni2, content='Looking for job opportunities.', likes=5, dislikes=1)

        AlumniFeedback.objects.create(subject='Great event!', category='EVENT', message='Loved the alumni meet.')
        AlumniFeedback.objects.create(subject='Website suggestion', category='WEBSITE', message='Add more resources.')

        job1 = JobBoard.objects.create(
            job_title='Backend Developer', job_location='Remote', description='Work on backend systems.',
            job_type='Full-time', company_name='TechCorp', alumni_id=alumni1, app_url='https://apply.techcorp.com', date_posted=timezone.now()
        )
        job1.skills_required.add(alumni_skill_python)

        job2 = JobBoard.objects.create(
            job_title='Project Manager', job_location='Onsite', description='Manage projects.',
            job_type='Contract', company_name='BizInc', alumni_id=alumni2, app_url='https://apply.bizinc.com', date_posted=timezone.now()
        )
        job2.skills_required.add(alumni_skill_leadership)

        Application.objects.create(alumni_id=alumni1, job_id=job1, status='pending')
        Application.objects.create(alumni_id=alumni2, job_id=job2, status='accepted')

        # --- Student App Sample Data ---
        skill_python = Skill.objects.create(name='Python')
        skill_django = Skill.objects.create(name='Django')
        skill_ml = Skill.objects.create(name='Machine Learning')

        student1 = Student.objects.create(name='Alice', year=2023)
        student2 = Student.objects.create(name='Bob', year=2024)
        student1.skills.add(skill_python, skill_django)
        student2.skills.add(skill_ml)

        mentorship_mentor = mentor1  # Use mentor from alumni app
        MentorshipRequest.objects.create(student=student1, mentor=mentorship_mentor, status='pending')

        internship1 = Internship.objects.create(title='Web Dev Intern', company='TechCorp', description='Work on web apps.')
        internship1.skills_required.add(skill_python, skill_django)

        InternshipApplication.objects.create(student=student1, internship=internship1, status='pending')

        training1 = Training.objects.create(title='ML Bootcamp', description='Intro to ML', duration_weeks=6)
        training1.skills_covered.add(skill_ml)

        TrainingEnrollment.objects.create(student=student2, training=training1)

        StudentFeedback.objects.create(student=student1, category='training', description='Great training!', rating=5)
        StudentFeedback.objects.create(student=student2, category='internship', description='Good experience.', rating=4)

        self.stdout.write(self.style.SUCCESS('Sample data for all apps loaded successfully.'))
