from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class stream(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class department(models.Model):
    stream_of = models.ForeignKey(stream, on_delete=models.SET_NULL, null=True, blank=True)
    dept_name = models.CharField(max_length=50)
    dept_pseudo = models.CharField(max_length=10)
    HoD = models.ForeignKey("authentication.SiteUser", on_delete=models.SET_NULL, null=True, related_name="hod", blank=True)
    
    def __str__(self):
        return self.dept_name
    
class staff_designation(models.Model):
    designation = models.CharField(max_length=20)
    
    def __str__(self):
        return self.designation
    
class SiteUser(AbstractUser):
    first_name = None
    last_name = None
    full_name = models.CharField(max_length=100)
    department = models.ForeignKey(department, on_delete=models.SET_NULL, null=True)
    yos = models.CharField(choices=(
        ("FIRST", "First Year"),
        ("SECOND", "Second Year"),
        ("THIRD", "Third Year"),
        ("FINAL", "Final Year")
    ), max_length=10, null=True, blank=True)
    contact = models.CharField(max_length=12)
    collegemail = models.EmailField(blank=True)
    user_type = models.CharField(max_length=50, choices=[
        ['FACULTY', 'Faculty'],
        ['RESEARCH SCHOLAR', 'Research Scholar'],
        ['STUDENT', 'Student'],
    ], default="STUDENT")
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    
    faculty = models.BooleanField(default=False)
    staff_designation = models.ForeignKey(staff_designation, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(_("email address"))
    
    # EMAIL_FIELD = "personalmail"
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    EMAIL_FIELD = 'email'
    
    def __str__(self):
        return self.username