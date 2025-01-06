from django.contrib import admin
from .models import Food, Reservation
from django.utils.translation import gettext_lazy as _

# --- Food Admin ---
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'formatted_price')  # نمایش نام غذا و قیمت
    search_fields = ('name',)  # جستجو بر اساس نام غذا
    list_filter = ('price',)  # فیلتر بر اساس قیمت
    ordering = ('name',)  # مرتب‌سازی بر اساس نام غذا به صورت صعودی
    list_per_page = 20  # نمایش 20 رکورد در هر صفحه

    def formatted_price(self, obj):
        return f"${obj.price:.2f}"  # فرمت کردن قیمت به دلار
    formatted_price.short_description = _('Formatted Price')

# --- Reservation Admin ---
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('username', 'food_name', 'reservation_date', 'price')  # نمایش نام کاربر، نام غذا و تاریخ رزرو
    search_fields = ('username__username', 'food_name__name')  # جستجو بر اساس نام کاربری و نام غذا
    list_filter = ('reservation_date', 'food_name__price')  # فیلتر بر اساس تاریخ رزرو و قیمت غذا
    ordering = ('-reservation_date',)  # مرتب‌سازی بر اساس تاریخ رزرو به صورت نزولی
    date_hierarchy = 'reservation_date'  # فیلتر کردن بر اساس تاریخ رزرو
    list_per_page = 20  # نمایش 20 رکورد در هر صفحه

    def price(self, obj):
        return obj.food_name.price  # نمایش قیمت غذا در رزرو
    price.short_description = _('Food Price')

    def reservation_date(self, obj):
        return obj.created_at  # فرض بر اینکه `created_at` در مدل `Reservation` وجود دارد
    reservation_date.admin_order_field = 'created_at'  # اجازه مرتب‌سازی بر اساس زمان رزرو

# ثبت مدل‌ها در ادمین
admin.site.register(Food, FoodAdmin)
admin.site.register(Reservation, ReservationAdmin)
