from django.db import models
from authentication.models import SiteUser



# Utility Classes
class GenericAchievement(models.Model):
    certificate = models.ForeignKey("core.Filelog", on_delete=models.CASCADE, related_name="%(class)s_certificate")
    support_docs = models.ForeignKey("core.Filelog", on_delete=models.SET_NULL, null=True, related_name="%(class)s_support_docs")
    team = models.ForeignKey("core.Team", on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField("core.Tags")
    
    created_by = models.ForeignKey(SiteUser, on_delete=models.CASCADE, related_name="%(class)s_createdby")
    created_timestamp = models.DateTimeField(auto_now_add=True)
    approved_by = models.ForeignKey(SiteUser, on_delete=models.SET_NULL, related_name="%(class)s_approver", null=True, blank=True)
    approval_timestamp = models.DateTimeField(blank=True)
    domain = models.ForeignKey("core.Domain", on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        abstract = True
    
class BaseAchievement(GenericAchievement):
    title = models.CharField(max_length=100)
    institution = models.CharField(max_length=300)
    organizer_name = models.CharField(max_length=100, help_text="Internal Sub Organization within institution", blank=True)
    from_date = models.DateField()
    to_date = models.DateField()
    class event_levels(models.TextChoices):
        INTERNATIONAL = ("INTERNATIONAL", "International")
        NATIONAL = ("NATIONAL", "National")
        STATE = ("STATE", "State")
        DISTRICT = ("DISTRICT", "District")
        ZONAL = ("ZONAL", "Zonal")
    class results(models.TextChoices):
        FIRST = ("FIRST", "First Prize")
        SECOND = ("SECOND", "Second Prize")
        THIRD = ("THIRD", "Third Prize")
        SPECIAL_MENTION = ("SPECIAL_MENTION", "Special Mention")
        PARTICIPATION = ("PARTICIPATION", "Participation")
        
    event_level = models.CharField(
        max_length=20,
        choices=event_levels.choices,
        default=event_levels.STATE,
    )
    result = models.CharField(
        max_length=20,
        choices=results.choices,
        default=results.PARTICIPATION,
        verbose_name="Achievement Outcome"
    )
                                      
    location_link = models.URLField(help_text="Event Venue Link")
    
    def __str__(self):
        return self.title
    class Meta:
        abstract = True

class Course_Provider(models.Model):
    provider_name = models.CharField(max_length=200)
    provider_link = models.URLField()
    
    def __str__(self):
        return self.provider_name
    
class Recognized_Student_Body(models.Model):
    organization_name = models.CharField(max_length=100)
    organization_link = models.URLField()
    global_chapter = models.BooleanField(help_text="Is it a National/Internation Student Chapter")
    organization_strength = models.IntegerField(help_text="Approximate count of members")
    

class Domain(models.Model):
    domain_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.domain_name

class Tags(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=100)
    
    created_by = models.ForeignKey(SiteUser, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.tag_name
    

class Team(models.Model):
    team_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    members = models.ManyToManyField("core.TeamMember")

class TeamMember(models.Model):
    member = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    
    def __str__(self):
        return self.member.full_name
    
class FileReasons(models.Model):
    reason = models.CharField(max_length=100)
    file_size = models.IntegerField(help_text="File Size In Bytes (1MB = 1000000 Bytes)")
    
    def __str__(self):
        return self.reason

class FileLog(models.Model):
    filename = models.CharField(max_length=100)
    reason = models.ForeignKey(FileReasons, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.filename