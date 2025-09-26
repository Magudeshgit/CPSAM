from django.db import models

from core.models import GenericAchievement, BaseAchievement, Course_Provider, Recognized_Student_Body

class Competition(BaseAchievement):
    def __str__(self):
        return self.title
    
class Workshop(BaseAchievement):
    team = result = None
    class mode(models.TextChoices):
        OFFLINE = ("OFFLINE", "Offline")
        ONLINE = ("ONLINE", "Online")
        HYBRID = ("HYBRID", "Hybrid")
    mode_of_work = models.CharField(max_length=50, choices=mode.choices)
        
        

class Course_Completion(BaseAchievement):
    team = organizer_name = brochures = participation_photos = event_id = None
    achievement_outcome = event_level = None
    verification_url = models.CharField(max_length=150, help_text="Certificate Verification URL or Code(if available)", null=True, blank=True)
    course_provider = models.ForeignKey(Course_Provider, on_delete=models.RESTRICT)
    
class Preplacement(BaseAchievement):
    result = event_level = institution = organizer_name = team = title = None
    brochures = participation_photos = event_id = None
     
    organization = models.CharField(max_length=300)
    class pp_type(models.TextChoices):
        INTERNSHIP = "INTERNSHIP", "Internship"
        APPRENTICESHIP = "APPRENTICESHIP", "Apprenticeship"
        FREELANCING = "FREELANCING", "Freelancing"
    ppo_type = models.CharField(max_length=50, choices=pp_type.choices)
    role = models.CharField(max_length=100, help_text="Describe your Role")
    github_link = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.organization
    
class Project(GenericAchievement):
    brochures = participation_photos = event_id = certificate = None
    title = models.CharField(max_length=200)
    problem_statement = models.TextField(help_text="Describe the problem statement")
    class project_types(models.TextChoices):
        SOFTWARE = "SOFTWARE", "Software"
        HARDWARE = "HARDWARE", "Hardware"
    project_type = models.CharField(max_length=50, choices=project_types.choices)
    github_link = models.URLField(null=True, blank=True)
    # prototype_video = models.URLField()
    prototype_video = models.FileField(upload_to="project_videos/")
    
    
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
    