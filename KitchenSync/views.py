from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, LoginForm
from .models import User

def home(request):
    return render(request, 'KitchenSync/home.html')

def addKitchen(request):
    return render(request, 'KitchenSync/addKitchen.html')

def viewKitchen(request):
    return render(request, 'KitchenSync/viewKitchen.html')

def weeklyPlanner(request):
    return render(request, 'KitchenSync/weeklyPlanner.html')

def login(request):
    return render(request, 'KitchenSync/login.html')

def register(request):
    return render(request, 'KitchenSync/register.html')

def userLogin(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user:
            auth_login(request, user)
            return redirect('KitchenSync/home.html')
        else:
            form.add_error(None, "Invalid username or password")
    return render(request, 'KitchenSync/login.html', {'form': form})

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.save()
            registered = True
    else:
        user_form = CustomUserCreationForm()

    return render(request, 'KitchenSync/register.html', {
        'user_form': user_form,
        'registered': registered
    })

@login_required
def logout_user(request):
    auth_logout(request)
    return redirect('KitchenSync/home.html')


