from django.db import models
from account.models import User

class Poll(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.text[:50]

class Poll_comment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, related_name='comments', on_delete=models.CASCADE) 
    text = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.text[:50]

class Notification(models.Model):
    number = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.text[:50] 



class Notification_User(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)  
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)  # ارتباط با اعلان
    is_read = models.BooleanField(default=False)  # وضعیت خوانده شده یا نشده
    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ ارتباط
    updated_at = models.DateTimeField(auto_now=True)  # تاریخ آخرین به‌روزرسانی ارتباط

    def __str__(self):
        return f"{self.username.username} - {self.notification.text[:50]}"


