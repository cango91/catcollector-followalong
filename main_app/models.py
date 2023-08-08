from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse

from datetime import date

# Create your models here.


class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    age = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.id}: {self.name}, {self.breed}, {self.age} y.o."

    def get_absolute_url(self):
        return reverse("cats:detail", kwargs={"cat_id": self.id})

    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)


MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)


class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(max_length=1,
                            choices=MEALS,
                            default=MEALS[0][0])
    # create a cat_id FK
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
