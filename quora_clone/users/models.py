from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class EndUser(User):
    GENDER_CHOICES = [
        ('M', "Male"),
        ('F', "Female"),
        ('O', "Others"),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    