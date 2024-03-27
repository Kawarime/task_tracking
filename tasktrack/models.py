from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    status = models.CharField(max_length = 50)



class Task(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    staus = models.ForeignKey(Status, on_delete = models.DO_NOTHING)
    owner = models.ManyToManyField(User)
    priority = models.IntegerField()
    start_date = models.DateField()
    dead_line = models.DateField()
