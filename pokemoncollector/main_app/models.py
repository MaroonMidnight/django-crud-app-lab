from django.db import models
from django.urls import reverse

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=50)
    effect = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("item-detail", kwargs={"pk": self.id})
    


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    evolution = models.IntegerField()
    
    items = models.ManyToManyField(Item)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("pokemon-detail", kwargs={"pokemon_id": self.id})
    
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
    )
    
class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"