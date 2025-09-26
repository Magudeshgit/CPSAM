from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from rest_framework.routers import DefaultRouter, SimpleRouter

from .auth_views import *
from .views import OperationsViewSet

router = DefaultRouter()
router.register(r'authentication', User_Accounts, basename='User Accounts')
router.register(r'operations', viewset=OperationsViewSet, basename="ops")

urlpatterns = [
    path("", include(router.urls)),
]
