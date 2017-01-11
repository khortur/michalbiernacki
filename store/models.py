from django.db import models
from datetime import date
import sys
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Mattress(models.Model):
    name = models.CharField(max_length=200)
    width = models.IntegerField(validators=[MinValueValidator(70),MaxValueValidator(200)], default=90)
    height = models.IntegerField(validators=[MinValueValidator(180),MaxValueValidator(220)], default=200)
    thickness = models.IntegerField(validators=[MinValueValidator(3),MaxValueValidator(50)], default=20)
    description = models.TextField()
    publish_date = models.DateField(default=timezone.now)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=0)