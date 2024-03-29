from django.urls import path
from tasktrack.views import *

urlpatterns = [
    path('', index, name = "index"),
    path('detail/<int:task_id>/', task_detail, name = "task_detail"),
    path('task_add/', task_add, name="task_add"),
    path('task_edit/<int:task_id>/', task_edit, name = "task_edit")
]
