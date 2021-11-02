from django.db import models
from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'),
    ('S', 'Second Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    beaklength= models.CharField(max_length=100)
    age = models.IntegerField()
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})

class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(max_length=1)