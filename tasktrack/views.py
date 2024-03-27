from django.shortcuts import render
from tasktrack.models import *

def index(request):
    task = Task.objects.all()
    context = {"task":task}
    return render(request, "tasktrack/index.html", context)


