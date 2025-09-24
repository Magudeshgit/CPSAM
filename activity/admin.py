from django.contrib import admin
from .models import *


admin.site.register([Competition, Course_Completion, Workshop, Preplacement, Project, Social_Service, StudentBody, ActivityManager])