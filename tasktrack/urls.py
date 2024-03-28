from django.urls import path
from tasktrack.views import *

urlpatterns = [
    path('', index, name = "index"),
    path('detail/<int:task_id>/', task_detail, name = "task_detail"),
]
