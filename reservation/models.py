from django.db import models
from account.models import User



class Food(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    food_name = models.ForeignKey(Food, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)








