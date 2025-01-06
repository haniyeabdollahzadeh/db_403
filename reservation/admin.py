from django.contrib import admin
from .models import Food, Reservation
from django.utils.html import format_html

# مدل غذا در پنل ادمین
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at', 'updated_at')  # نمایش فیلدهای مربوطه در لیست
    search_fields = ('name',)  # جستجو بر اساس نام غذا
    list_filter = ('created_at',)  # فیلتر بر اساس تاریخ ایجاد
    ordering = ('-created_at',)  # مرتب‌سازی بر اساس تاریخ ایجاد
    readonly_fields = ('created_at', 'updated_at')  # نمایش فقط خواندنی فیلدهای تاریخ

# مدل رزرو در پنل ادمین
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('username', 'food_name', 'quantity', 'total_price', 'created_at', 'updated_at')  # نمایش فیلدهای رزرو
    search_fields = ('username__username', 'food_name__name')  # جستجو بر اساس نام کاربری و نام غذا
    list_filter = ('created_at',)  # فیلتر بر اساس تاریخ رزرو
    ordering = ('-created_at',)  # مرتب‌سازی بر اساس تاریخ رزرو
    readonly_fields = ('created_at', 'updated_at', 'total_price')  # نمایش فقط خواندنی فیلدهای تاریخ و قیمت کل

    def total_price(self, obj):
        return f"{obj.total_price:.2f} USD"  # نمایش قیمت کل با دو رقم اعشار
    total_price.admin_order_field = 'total_price'  # امکان مرتب‌سازی بر اساس قیمت کل

# ثبت مدل‌ها در پنل ادمین
admin.site.register(Food, FoodAdmin)
admin.site.register(Reservation, ReservationAdmin)
