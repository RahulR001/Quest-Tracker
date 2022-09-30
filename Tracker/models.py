from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

design_choice = (
    ('', '-----Select Designationr-----'),
    ('manager','Manager'),
    ('team lead','Team Lead'),
    ('developer','Developer')
)

status_choice=(
    ('working on it','Working on it'),
    ('stuck','Stuck'),
    ('done','Done')
)


class new_user(AbstractUser):
    designation = models.CharField(max_length=30,choices=design_choice, default=False)
    profile = models.ImageField(default=False,upload_to='avatars')
 

 
# ========== class-to-generate-task-table ==========

class Task(models.Model):
    unique_user = models.ForeignKey(new_user, on_delete=models.CASCADE)
    tasktitle = models.CharField(max_length=30)
    taskDesc = models.TextField(blank=True)
    developer = models.CharField(max_length=30, blank=True )
    status = models.CharField(max_length=30,choices=status_choice,default='Working on it')
    created_time = models.TimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    deadline = models.DateField()
