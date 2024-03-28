from django.shortcuts import render
from tasktrack.models import *

def index(request):
    task = Task.objects.all()
    context = {"task":task}
    return render(request, "tasktrack/index.html", context)


def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    context = {"task":task}
    return render(request, "tasktrack/detail.html", context=context)