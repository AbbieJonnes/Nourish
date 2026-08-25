from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
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