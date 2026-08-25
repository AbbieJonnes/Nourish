from django.db import models
# Create your models here.
from django.contrib.auth.models import User


class FoodItem(models.Model):
    MEAL_CHOICES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snack', 'Snack'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)

    calories = models.PositiveIntegerField()

    meal_type = models.CharField(
        max_length=20,
        choices=MEAL_CHOICES
    )

    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
