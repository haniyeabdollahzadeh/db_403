"""from django.contrib import admin
from .models import Transaction
from django.utils.translation import gettext_lazy as _

# --- Transaction Admin ---
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('Tnumber', 'username', 'amount', 'formatted_amount', 'transaction_date')  # نمایش شماره تراکنش، نام کاربر، مبلغ و تاریخ
    search_fields = ('Tnumber', 'username__username')  # جستجو بر اساس شماره تراکنش و نام کاربر
    list_filter = ('transaction_date',)  # فیلتر بر اساس تاریخ تراکنش
    ordering = ('-transaction_date',)  # مرتب‌سازی بر اساس تاریخ تراکنش به صورت نزولی
    date_hierarchy = 'transaction_date'  # فیلتر کردن بر اساس تاریخ تراکنش
    list_per_page = 20  # نمایش 20 رکورد در هر صفحه

    def formatted_amount(self, obj):
        return f"${obj.amount:.2f}"  # فرمت کردن مبلغ به دلار
    formatted_amount.short_description = _('Formatted Amount')

    def transaction_date(self, obj):
        return obj.created_at  # فرض بر اینکه `created_at` در مدل `Transaction` وجود دارد
    transaction_date.admin_order_field = 'created_at'  # اجازه مرتب‌سازی بر اساس زمان تراکنش

# ثبت مدل‌ها در ادمین
admin.site.register(Transaction, TransactionAdmin)
"""