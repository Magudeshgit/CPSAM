from django.contrib import admin
from .models import *

admin.site.register([Domain, Tags, Team, TeamMember, FileReasons, FileLog, Course_Provider])
