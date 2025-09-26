from django.shortcuts import render
from activity.models import *
from .models import AcademicYear
def dashboard(request):
    activities = ActivityManager.objects.all()
    ays = AcademicYear.objects.all().order_by("-current")
    return render(request, "core/dashboard.html", {"activities": activities, "ays":ays})