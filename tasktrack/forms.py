from django import forms
from tasktrack.models import Task

class TaskAdd(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "status", "priority", "start_date", "dead_line"]
