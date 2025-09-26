from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *
def signup(request):
    if (request.user.is_authenticated): return redirect("home")
    errors = ""
    if request.method == 'POST':
        # if form.is_valid():
        try:
            user = SiteUser.objects.create_user(
                        username = request.POST['personalmail'] if request.POST.get('usertype') == "faculty" else request.POST['roll'],
                        email = request.POST['personalmail'],
                        collegemail = request.POST['personalmail'],
                        full_name = request.POST['fullname'],
                        department = department.objects.get(id = int(request.POST['department'])),
                        yos = None if request.POST.get('usertype') == "faculty" else request.POST['yos'],
                        contact = request.POST['contact'],
                        password = request.POST['password1'], 
                        user_type = "FACULTY" if request.POST.get('usertype') == "faculty" else "STUDENT",
                        profile_photo = request.FILES['profile_photo'] if 'profile_photo' in request.FILES else None,
                        faculty = True if request.POST.get('usertype') == "faculty" else False,
                        staff_designation = staff_designation.objects.get(id = int(request.POST['department'])) if request.POST.get('usertype') == "faculty" else None
                    )
            user.save()
            login(request, user)
            try:
                red = request.GET['next']
                return redirect(red)
            except:
                return redirect('/')
        except IntegrityError:
            errors = f"User Already Exists with the same {'Email Address' if request.POST.get('usertype') == 'faculty' else 'Register Number'}"
    return render(request, "authentication/signup.html", {"departments": department.objects.all().reverse(),
                                                          "staffdesignations": staff_designation.objects.all().reverse(),
                                                          "errortext": errors
                                                          })
    
def signin(request):
    error = ""
    if request.method == "POST":
        print(request.POST['username'], request.POST['password'])
        auth = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if auth is not None:
            login(request, auth)
            try:
                red = request.GET['next']
                return redirect(red)
            except:
                return redirect('home')
        else:
            error = "Incorrect Username or Password"
    return render(request, "authentication/signin.html", {"error": error})

class password_reset(SuccessMessageMixin, PasswordResetView):
    template_name = 'authentication/password_reset.html'
    email_template_name = 'authentication/password_reset_mail.html'
    subject_template_name = 'authentication/password_reset_email_subject.txt'
    success_url  = reverse_lazy('passwordresetmailsent')


def passwordResetMailSent(request):
    return render(request, 'authentication/password_reset_mail_sent.html')

@login_required
def profile(request):
    forms = UserUpdateForm(instance=request.user)
    if request.method == "POST":
        forms = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if forms.is_valid():
            forms.save()
            messages.add_message(request, level=messages.INFO, message="Profile Successfully Updated")
        else:
            print(forms.errors)
            
    return render(request, "authentication/profile.html", {"forms": forms})

def user_logout(request):
    logout(request)
    return redirect("signup")