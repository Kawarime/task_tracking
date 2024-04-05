from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    STATUSES= [
        ("notdone", "Not Done"),
        ("in_progress", "In Progress"),
        ("done", "Done")
    ]
    name = models.CharField(max_length = 50)
    description = models.TextField()
    status = models.CharField(max_length = 50, choices = STATUSES, default = "notdone")
    priority = models.IntegerField()
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    start_date = models.DateField()
    dead_line = models.DateField()

    def __str__(self):
        return f"{self.name}"