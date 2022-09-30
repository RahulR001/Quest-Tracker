from django.shortcuts import render, redirect
from .forms import NewUser, TaskForm
from .models import new_user, Task 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as user_login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


 
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
