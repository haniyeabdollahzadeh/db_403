from django.db import models
from account.models import User



class Food(models.Model):
    name = models.CharField(max_length=100)  # نام غذا
    price = models.FloatField()  # قیمت غذا
    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ ایجاد غذا
    updated_at = models.DateTimeField(auto_now=True)  # تاریخ آخرین به‌روزرسانی

    def __str__(self):
        return self.name


class Reservation(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)  # نام کاربری که رزرو کرده است
    food_name = models.ForeignKey(Food, on_delete=models.CASCADE)  # غذایی که رزرو شده است
    quantity = models.PositiveIntegerField(default=1)  # تعداد غذاهای رزرو شده
    total_price = models.FloatField()  # قیمت کل رزرو (قیمت غذا * تعداد)
    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ رزرو
    updated_at = models.DateTimeField(auto_now=True)  # تاریخ آخرین به‌روزرسانی رزرو

    def save(self, *args, **kwargs):
        # محاسبه قیمت کل هر رزرو بر اساس تعداد و قیمت غذا
        self.total_price = self.food_name.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reservation by {self.username.username} for {self.food_name.name} ({self.quantity} items)"







