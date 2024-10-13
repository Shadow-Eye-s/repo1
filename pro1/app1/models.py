
# models.py
from django.db import models

class Person(models.Model):
    age = models.IntegerField()

    def __str__(self):
        return f"Age: {self.age}"


# Create your models here.
