from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, FoodItemForm
from .models import FoodItem


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')

    else:
        form = RegisterForm()

    return render(request, 'calorie_tracker/register.html', {
        'form': form
    })

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        return render(request, 'calorie_tracker/login.html', {
            'error': 'Invalid username or password.'
        })

    return render(request, 'calorie_tracker/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def add_food(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)

        if form.is_valid():
            food = form.save(commit=False)
            food.user = request.user
            food.save()

            return redirect('dashboard')

    else:
        form = FoodItemForm()

    return render(request, 'calorie_tracker/add_food.html', {
        'form': form
    })

@login_required
def delete_food(request, food_id):
    food = get_object_or_404(
        FoodItem,
        id=food_id,
        user=request.user
    )

    if request.method == 'POST':
        food.delete()

    return redirect('dashboard')

@login_required
def dashboard(request):
    foods = FoodItem.objects.filter(
        user=request.user
    ).order_by('-date_added', '-id')

    total_calories = sum(food.calories for food in foods)

    return render(request, 'calorie_tracker/dashboard.html', {
        'foods': foods,
        'total_calories': total_calories,
    })