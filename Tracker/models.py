from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

design_choice = (
    ('',''),
    ('manager','Manager'),
    ('team lead','Team Lead'),
    ('developer','Developer')
)

class new_user(AbstractUser):
    designation = models.CharField(max_length=30,choices=design_choice, default=False)
    profile = models.ImageField(default=False,upload_to='avatars')
 


# ========== class-to-generate-task-table ==========

class Task(models.Model):
    unique_user = models.ForeignKey(new_user, on_delete=models.CASCADE)
    tasktitle = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    created_time = models.TimeField(auto_now_add=True)
    completed = models.BooleanField()
    deadline = models.DateField()
