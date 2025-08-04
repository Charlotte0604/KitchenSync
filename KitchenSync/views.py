from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Ingredient, UserIngredient
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import get_user_model
User = get_user_model()

def home(request):
    return render(request, 'KitchenSync/home.html')

@login_required
def addKitchen(request):
    if request.method == 'POST':
        ingredient_names = request.POST.getlist('ingredients')
        for name in ingredient_names:
            quantity = request.POST.get(f'quantity_{name}', '')

            # Get or create the Ingredient
            ingredient, _ = Ingredient.objects.get_or_create(name=name)

            # Create or update UserIngredient
            UserIngredient.objects.update_or_create(
                user=request.user,
                ingredient=ingredient,
                defaults={'quantity': quantity}
            )
        return redirect('viewKitchen')  # or wherever you want to go after saving

    all_ingredients = Ingredient.objects.all()
    return render(request, 'KitchenSync/addKitchen.html', {
        'all_ingredients': all_ingredients
    })

@login_required
def viewKitchen(request):
    user_ingredients = UserIngredient.objects.filter(user=request.user)
    return render(request, 'KitchenSync/viewKitchen.html', {
        'user_ingredients': user_ingredients
    })


def weeklyPlanner(request):
    return render(request, 'KitchenSync/weeklyPlanner.html')

def userLogin(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user:
            auth_login(request, user)
            return redirect('home')
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
    return redirect('home')


