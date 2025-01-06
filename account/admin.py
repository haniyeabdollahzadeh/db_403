"""from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _

# --- Custom User Admin ---
class CustomUserAdmin(UserAdmin):
    # نمایش فیلدهای مدل در لیست ادمین
    list_display = ('username', 'email', 'phone', 'access_level', 'credit', 'date_joined', 'last_login')
    
    # فیلدهایی که می‌توان در آنها جستجو کرد
    search_fields = ('username', 'email', 'phone')  # جستجو بر اساس نام کاربری، ایمیل و شماره تلفن

    # فیلتر کردن کاربران بر اساس سطح دسترسی
    list_filter = ('access_level', 'is_active', 'is_staff')

    # مرتب‌سازی کاربران به ترتیب نزولی بر اساس تاریخ ثبت‌نام
    ordering = ('-date_joined',)

    # تنظیمات خاص برای فرم تغییر و ایجاد
    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'email', 'phone', 'access_level', 'credit')
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined')
        }),
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2', 'phone', 'access_level', 'credit')
        }),
    )

    # این قابلیت به شما این امکان را می‌دهد که تاریخ و زمان آخرین ورود و تاریخ ثبت‌نام را نمایش دهید
    def credit_in_usd(self, obj):
        return f"${obj.credit:.2f}"  # نمایش اعتبار به دلار
    credit_in_usd.short_description = _('Credit (USD)')

# ثبت مدل در ادمین با استفاده از کلاس ادمین سفارشی
admin.site.register(User, CustomUserAdmin)
"""