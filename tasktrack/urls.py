from django.urls import path
from tasktrack.views import *

urlpatterns = [
    path('', TaskListView.as_view(), name = "task_list"),
    path('<int:pk>/', TaskDetailView.as_view(), name = "task_detail"),
    path('task_add/', TaskAddView.as_view(), name="task_add"),

]

app_name = "tasktrack"
