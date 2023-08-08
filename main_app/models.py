from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse

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
    