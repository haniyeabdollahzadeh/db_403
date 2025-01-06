from django.db import models

class User (models.Model):

    LEVEL_CHOICES = (
        ("A", "admin"),
        ("U", "user")
    )
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=15)
    access_level = models.CharField(max_length=1, choices=LEVEL_CHOICES)
    credit = models.FloatField()

 

  


