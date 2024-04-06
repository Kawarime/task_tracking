from django.shortcuts import render
from tasktrack.models import *
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from tasktrack.forms import TaskAdd
from django.contrib.auth.mixins import LoginRequiredMixin
from tasktrack.mixins import *


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "tasktrack/task_list.html"

class TaskDetailView(DetailView):
    model = Task
    template_name = "tasktrack/task_detail.html"
    context_object_name = "tasks"

class TaskAddView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasktrack/task_add.html"
    form_class = TaskAdd
    success_url = "/"

class TaskUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Task
    template_name = "tasktrack/task_update.html"
    form_class = TaskAdd
    succes_url = "/"


class TaskDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Task
    template_name = "tasktrack/task_delete.html"
    succes_url = "/"

    