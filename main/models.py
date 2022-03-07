from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from django.db.models import Model


class Student(Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    age = models.IntegerField(default=17, validators=[MinValueValidator(17)])