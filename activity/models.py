from django.db import models

from core.models import GenericAchievement, BaseAchievement, Course_Provider, Recognized_Student_Body

class Competition(BaseAchievement):
    def __str__(self):
        return self.title
    
class Workshop(BaseAchievement):
    team = None
    class mode(models.TextChoices):
        OFFLINE = ("OFFLINE", "Offline")
        ONLINE = ("ONLINE", "Online")
        HYBRID = ("HYBRID", "Hybrid")
    class result(models.TextChoices):
        SPECIAL_MENTION = ("SPECIAL_MENTION", "Special Mention")
        PARTICIPATION = ("PARTICIPATION", "Participation")
        

class Course_Completion(BaseAchievement):
    team = organizer_name = None
    verification_url = models.CharField(max_length=150, help_text="Certificate Verification URL or Code(if applicable)", null=True, blank=True)
    course_provider = models.ForeignKey(Course_Provider, on_delete=models.RESTRICT)
    
class Preplacement(BaseAchievement):
    result = event_level = institution = organizer_name = team = None
    organization = models.CharField(max_length=300)
    class pp_type(models.TextChoices):
        INTERNSHIP = "INTERNSHIP", "Internship"
        APPRENTICESHIP = "APPRENTICESHIP", "Apprenticeship"
        FREELANCING = "FREELANCING", "Freelancing"
    role = models.CharField(max_length=100, help_text="Describe your Role")
    github_link = models.URLField()
    
class Project(GenericAchievement):
    title = models.CharField(max_length=200)
    problem_statement = models.TextField(help_text="Describe the problem statement")
    class project_type(models.TextChoices):
        SOFTWARE = "SOFTWARE", "Software"
        HARDWARE = "HARDWARE", "Hardware"
    github_link = models.URLField()
    prototype_video = models.URLField()
    
    def __str__(self):
        return self.title
    
class StudentBody(GenericAchievement):
    organization = models.ForeignKey(Recognized_Student_Body, on_delete=models.RESTRICT)
    from_date = models.DateField(help_text="Tenure of service")
    to_date = models.DateField()
    role = models.CharField(max_length=100)
    recognized_student_chap = models.BooleanField()
    
    def __str__(self):
        return self.organization.organization_name

class Social_Service(models.Model):
    organization_name = models.CharField(max_length=200)
    organization_link = models.URLField()
    tenure_from = models.DateField(help_text="Tenure of service")
    tenure_to = models.DateField()
    role = models.CharField(max_length=100)
    
    def __str__(self):
        return self.organization_name
    
    
class ActivityManager(models.Model):
    activity_name = models.CharField(max_length=100)
    url_name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, help_text="filename")
    additional_text = models.TextField()
    
    def __str__(self):
        return self.activity_name
    