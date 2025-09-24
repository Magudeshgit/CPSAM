from django.urls import include, path
from .views import *

urlpatterns = [
    path("add/<int:activity_id>", add_activity, name="add_activity")
]