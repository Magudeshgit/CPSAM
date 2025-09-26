from django.shortcuts import render
from activity.models import *
from .models import AcademicYear
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    activities = ActivityManager.objects.all()
    ays = AcademicYear.objects.all().order_by("-current")
    return render(request, "core/dashboard.html", {"activities": activities, "ays":ays})