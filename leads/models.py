from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save  # a add information after it is saved to db


# User = get_user_model() # this is default user_model from django, Not Recommended.


class User(AbstractUser):
    """
    Custom User model from auth.models AbstractUser
    """
    # User will be the organizer when it is first created
    is_organizer = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)
    phone_nr = models.CharField(max_length=20)


class UserProfile(models.Model):
    """A profile class that have one User."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # all details are taken from the user model

    def __str__(self):
        return self.user.username


class Agent(models.Model):
    """
    Agent model, each  have a name, last name and phone number/optional from the User logged in to the system.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


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
    age = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
    phone_nr = models.CharField(max_length=20)

    phoned = models.BooleanField(default=False)

    sources = models.CharField(
        choices=SOURCE_CHOICES,
        max_length=128
    )

    profile_picture = models.ImageField(blank=True, null=True)
    special_files = models.FileField(blank=True)

    # foreignKey to agent, on_delete set to null, null value must be True for this.
    agent = models.ForeignKey('Agent', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}, phone_nr: {self.phone_nr}, Source: {self.sources}'


def post_user_created_signal(sender, instance, created, **kwargs):
    """Create a user profile in the moment a user is created using signals."""
    print(instance, created)
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)
