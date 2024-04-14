from django import forms
from tasktrack.models import Task, Comment

class TaskAdd(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "status", "priority", "start_date", "dead_line", "creator"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]