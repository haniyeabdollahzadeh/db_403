from django.db import models
from account.models import User



class Food(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()


class reservation(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    food_name = models.ForeignKey(Food, on_delete=models.CASCADE)









