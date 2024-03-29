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
    
def task_edit(request, task_id, task_name, task_descriprion, task_staus, task_owner, task_priority, task_start_date, task_dead_line):
    task = Task.objects.get(id=task_id)
    name = Task.objects.get(name = task_name)
    descriprion = Task.objects.get(description = task_descriprion)
    staus = Task.objects.get(staus = task_staus)
    owner = Task.objects.get(owner = task_owner)
    priority = Task.objects.get(priority = task_priority)
    start_date = Task.objects.get(start_date = task_start_date)
    dead_line = Task.objects.get(dead_line = task_dead_line)
    return render(request, "tasktrack/task_edit.html")


