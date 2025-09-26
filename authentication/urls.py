
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from django.conf import settings
from django.conf.urls.static import static

from core.views import *
from authentication.views import *

urlpatterns = [
    path("", view=signup),
    path("signup/", view=signup, name="signup"),
    path("signin/", view=signin, name="signin"),
    path("logout/", view=user_logout, name="logout"),
    
    
    path('forgot_password/', view=password_reset.as_view(), name="password_reset"),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="authentication/password_reset_confirm.html"), name="password_reset_confirm"),
    path('password-reset-mail-sent/', passwordResetMailSent, name='passwordresetmailsent'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name="authentication/password_reset_complete.html"), name="password_reset_complete"),
    
    path("profile/", view=profile, name="profile"),
]


