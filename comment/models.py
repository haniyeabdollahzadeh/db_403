from django.db import models
from account.models import User

class Poll(models.Model):
    poll_number = models.IntegerField()
    text = models.TextField()


class Poll_comment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)


class Notification(models.Model):
    number = models.IntegerField()
    text = models.TextField()



class Notification_User(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.ForeignKey(Notification, on_delete=models.CASCADE)
    
