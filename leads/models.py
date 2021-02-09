from django.db import models

# Create your models here.


class Lead(models.Model):
    """A Lead database with first name, last name and age."""
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    age = models.IntegerField(default=0)

