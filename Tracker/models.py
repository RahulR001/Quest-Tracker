from django.db import models
from django.contrib.auth.models import User


class new_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=False)
    designation = models.CharField(max_length=30, default=False)
    profile = models.FileField(default=False)


# ========== class-to-generate-task-table ==========

class Task(models.Model):
    unique_user = models.ForeignKey(new_user, on_delete=models.CASCADE)
    tasktitle = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    created_time = models.TimeField(auto_now_add=True)
    completed = models.BooleanField()
    deadline = models.DateField()
