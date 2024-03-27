from django.urls import path
from tasktrack.views import *

urlpatterns = [
    path('', index, name = "index"),
]
