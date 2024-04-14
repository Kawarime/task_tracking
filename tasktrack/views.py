from django.shortcuts import render
from tasktrack.models import *
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from tasktrack.forms import TaskAdd, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from tasktrack.mixins import *


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "tasktrack/task_list.html"

class TaskDetailView(DetailView):
    model = Task
    template_name = "tasktrack/task_detail.html"
    context_object_name = "task"

    #def get_context_data(self, **kwargs)
    #    context = super().get_context_data(**kwargs)
    #    context ["comments"] = Comment.objects.filter(task=self.get_object())
    #    return context

class TaskAddView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasktrack/task_add.html"
    form_class = TaskAdd
    success_url = "/"

class TaskUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Task
    template_name = "tasktrack/task_update.html"
    form_class = TaskAdd
    success_url = "/"

class TaskDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Task
    template_name = "tasktrack/task_delete.html"
    success_url = "/"

class CommentAddView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = "tasktrack/comment_add.html"
    form_class = CommentForm
    success_url = "/"
    
    #def form_valid(self, form):
    #    form.instance.author = self.request.user
    #    form.instance.task = get_object_or_404(Task, pk=self.kwargs.get('pk'))
    #    return super().form_valid(form)