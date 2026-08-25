from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import FoodItem


# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-4 py-3 rounded-xl border border-stone-200 focus:outline-none focus:ring-2 focus:ring-yellow-500',
            'placeholder': 'you@example.com'
        })
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 rounded-xl border border-stone-200 focus:outline-none focus:ring-2 focus:ring-yellow-500',
            'placeholder': 'Choose a username'
        })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 rounded-xl border border-stone-200 focus:outline-none focus:ring-2 focus:ring-yellow-500',
            'placeholder': 'Create a password'
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 rounded-xl border border-stone-200 focus:outline-none focus:ring-2 focus:ring-yellow-500',
            'placeholder': 'Confirm your password'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class FoodItemForm(forms.ModelForm):
#      class Meta:
#         model = FoodItem
#         fields = ['name', 'calories', 'meal_type']

class FoodItemForm(forms.ModelForm):

    class Meta:
        model = FoodItem
        fields = ['name', 'calories', 'meal_type']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-stone-200 focus:outline-none focus:ring-2 focus:ring-yellow-500',
                'placeholder': 'e.g. Grilled chicken'
            }),

            'calories': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-stone-200 focus:outline-none focus:ring-2 focus:ring-yellow-500',
                'placeholder': 'e.g. 450'
            }),

            'meal_type': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-stone-200 focus:outline-none focus:ring-2 focus:ring-yellow-500',
                'placeholder': 'e.g. Lunch'
            }),
        }