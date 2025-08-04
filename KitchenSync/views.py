from django.shortcuts import render

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


