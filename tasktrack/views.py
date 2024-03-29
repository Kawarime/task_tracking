from django.shortcuts import render, redirect
from tasktrack.models import *

def index(request):
    task = Task.objects.all()
    context = {"task":task}
    return render(request, "tasktrack/index.html", context)

def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    context = {"task":task}
    return render(request, "tasktrack/detail.html", context=context)

def task_add(request):
    if request.method == "POST":
        task_name = request.POST.get("task_name")
        task_description = request.POST.get("task_description")
        task_status = request.POST.get("task_status")
        task_owner = request.POST.get("task_owner")
        task_priority = request.POST.get("task_priority")
        task_deadline = request.POST.get("task_deadline")

        task = Task.objects.create(
            name=task_name,
            description=task_description,
            status=task_status,
            owner=task_owner,
            priority=task_priority,
            deadline = task_deadline
        )
        return redirect("task_detail", id=task.id)
    else:
        return render(request, template_name="tasktrack/task_add.html")