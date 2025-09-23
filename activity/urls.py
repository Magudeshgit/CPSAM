from django.urls import include, path
from .views import *

urlpatterns = [
    path("/", view=dashboard, name="dashboard")
]