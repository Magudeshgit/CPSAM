from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from rest_framework.routers import DefaultRouter

from .auth_views import *
from .views import *

router = DefaultRouter()
router.register(r'authentication', User_Accounts, basename='User Accounts')

urlpatterns = [
    path("", include(router.urls)),
]
