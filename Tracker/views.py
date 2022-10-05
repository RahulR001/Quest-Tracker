from django.shortcuts import render, redirect
from .forms import NewUser, TaskForm, UpdateForm
from .models import new_user, Task 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as user_login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def task(request):
    developers = new_user.objects.all()
    if request.user.is_authenticated:
        user = request.user
        print(user.designation)
        if user.designation == 'Manager' or user.designation == 'Team lead':
            if request.method == 'POST':
                form = TaskForm(request.POST)
                if form.is_valid():
                    task = form.save(commit=False)
                    task.unique_user = request.user
                    task.developer = request.POST.get('developer')
                    task.save()
                    return redirect('quest')
            else:
                form = TaskForm()
        else:
            return redirect('viewtask')
    else:
        form = TaskForm()
    return render(request, 'quest.html',{'form':form,'dev':developers})


@login_required(login_url='login')
def viewtask(request):
    if request.user.is_authenticated:
        user = request.user
        if user.designation == 'Developer':
            username = user.username
            designation = False
            tasks = Task.objects.filter(developer=username)
        else:
            tasks = Task.objects.all()
            designation = True
    return render(request, 'view_task.html', {'tasks': tasks, 'designation': designation})


@login_required(login_url='login')
def updatetask(request,id):
    ls = Task.objects.get(id=id)
    form = UpdateForm(request.POST or None, instance=ls)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('viewtask')
    return render(request, "update_task.html",{'ls':ls,'form':form})


@login_required(login_url='login')
def deletetask(request,id):
    ls = Task.objects.get(id=id)
    ls.delete()
    return redirect('viewtask')
# ========== method-to-access-login-view ==========


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            user_login(request, user)
            return redirect('quest')
        else:
            messages.error(request, 'Username and Password Incorrect')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


# ========== method-to-access-signup-view ==========

def signup(request):
    if request.method == "POST":
        form = NewUser(request.POST, request.FILES)
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        uname = new_user.objects.filter(username=username)
        if password1 == password2:
            if uname:
                messages.info(request, 'Username taken')
            elif form.is_valid():
                user = form.save()
                return redirect('/')
            else:
                messages.info(request, 'Password too short')
        else:
            messages.info(request, 'Password mismatch')
    else:
        form = NewUser()
    return render(request, 'registration/signup.html', {'form': form})
