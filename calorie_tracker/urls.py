from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add-food/', views.add_food, name='add_food'),
    path('delete-food/<int:food_id>/', views.delete_food, name='delete_food'),
    path('reset-day/', views.reset_day, name='reset_day'),
    path('', views.dashboard, name='dashboard'),
]