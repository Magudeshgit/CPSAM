from django.shortcuts import render
from activity.models import *
def dashboard(request):
    activities = ActivityManager.objects.all()
    return render(request, "core/dashboard.html", {"activities": activities})