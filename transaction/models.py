from django.db import models
from account.models import User


class Transaction(models.Model):
    Tnumber = models.IntegerField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
