from django.shortcuts import render
from .models import *
from .forms import *
ALL_ACTIVITIES = {
    "competition": {
        "model": Competition,
        "forms": CompetitionForm
    }
}
def dashboard(request):
    return render(request, "activity/dashboard.html")
def add_activity(request, activity_id:int):
    activity = ActivityManager.objects.get(id=activity_id)
    forms = ALL_ACTIVITIES.get(activity.activity_name.lower()).get("forms")
    if request.method == "POST":
        valid = forms(request.POST)
        print("hellp", valid.is_valid())
    return render(request, "activity/activity_add.html", {"form":forms, "activity": activity})