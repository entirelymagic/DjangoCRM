from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField

# User = get_user_model() # this is default user_model from django, Not Recommended.


class User(AbstractUser):
    """
    Custom User model from auth.models AbstractUser
    """
    phone_nr = PhoneField(blank=True, help_text="Contact phone number.")


class Agent(models.Model):
    """
    Agent model, each  have a name, last name and phone number/optional from the User logged in to the system.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Lead(models.Model):
    """A Lead database with first name, last name and age. Include a phoned boolean"""
    SOURCE_CHOICES = (
        ('Youtube', 'Youtube'),
        ('Google', 'Google'),
        ('Newsletter', 'Newsletter'),
        ('Linkedin', 'Linkedin'),
        ('Twitter', 'Twitter'),
        ('Other', 'Other'),
    )
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    age = models.IntegerField(default=0)
    phone_nr = PhoneField(blank=True, help_text="Contact phone number.")

    phoned = models.BooleanField(default=False)

    sources = models.CharField(
        choices=SOURCE_CHOICES,
        max_length=128
    )

    profile_picture = models.ImageField(blank=True, null=True)
    special_files = models.FileField()

    # foreignKey to agent, on_delete set to null, null value must be True for this.
    agent = models.ForeignKey('Agent', on_delete=models.SET_NULL, null=True)


