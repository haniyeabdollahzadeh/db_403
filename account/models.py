from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    LEVEL_CHOICES = (
        ("A", "admin"),
        ("U", "user")
    )
    
    phone = models.CharField(max_length=11,null=True,blank=True)
    access_level = models.CharField(max_length=1, choices=LEVEL_CHOICES,null=True,blank=True)
    credit = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)  

    def str(self):
        return self.username