from django.urls import path
from tasktrack.views import *

urlpatterns = [
    path('', TaskListView.as_view(), name = "task_list"),
    path('<int:pk>/', TaskDetailView.as_view(), name = "task_detail"),
    path('task_add/', TaskAddView.as_view(), name="task_add"),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name = "task_update"),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name = "task_delete"),
    path('comment_add/', CommentAddView.as_view(), name="comment_add"),

]

app_name = "tasktrack"
