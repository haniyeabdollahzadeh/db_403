from django.db import models
from django.contrib.auth.models import AbstractUser

class User (AbstractUser):

    LEVEL_CHOICES = (
        ("A", "admin"),
        ("U", "user")
    )
    
    phone = models.CharField(max_length=11)
    access_level = models.CharField(max_length=1, choices=LEVEL_CHOICES)
    credit = models.FloatField()

 

  


