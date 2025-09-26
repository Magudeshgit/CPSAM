from django.shortcuts import render, redirect
from .models import *
from .forms import *
from core.models import Tags, Domain
from authentication.models import SiteUser
from django.contrib.auth.decorators import login_required
ALL_ACTIVITIES = {
    "competition": {
        "model": Competition,
        "forms": CompetitionForm
    },
    "course completion": {
        "model": Course_Completion,
        "forms": CourseForm
    },
    "workshop/conferences": {
        "model": Workshop,
        "forms": WorkshopForm
    },
    "pre-placements": {
        "model": Preplacement,
        "forms": PPOForm
    },
    "project completion": {
        "model": Project,
        "forms": ProjectForm
    }
    
    
}

@login_required
def dashboard(request):
    return render(request, "activity/dashboard.html")

@login_required
def add_activity(request, activity_id:int):
    print(request.user.email)
    activity = ActivityManager.objects.get(id=activity_id)
    tags = Tags.objects.all()
    domains = Domain.objects.all()
    forms = ALL_ACTIVITIES.get(activity.activity_name.lower()).get("forms")
    if request.method == "POST":
        validation = forms(data=request.POST, files=request.FILES)
        if validation.is_valid():
            
            instance = validation.save(commit = False)
            instance.created_by = request.user
            instance.save()
            return redirect("home")
        else:
            forms = validation
            print(validation.errors)
    return render(request, "activity/activity_add.html", {"form":forms, "activity": activity, "tags":tags, "domains":domains})