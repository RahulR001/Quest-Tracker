from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Task,new_user


# ========== class-to-generate-task-from ==========

class TaskForm(forms.ModelForm):
    class Meta:
        model =  Task
        fields = ['tasktitle', 'status', 'completed', 'deadline']


# ========== class-to-generate-user-from ==========

class NewUser(UserCreationForm):
    class Meta:
        model = new_user
        fields = ['first_name', 'last_name', 'username',
                  'designation', 'profile', 'email', 'password1', 'password2']



 