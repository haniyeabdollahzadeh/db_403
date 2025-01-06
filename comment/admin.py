"""from django.contrib import admin
from .models import Poll, Poll_comment, Notification, Notification_User
from django.utils.html import format_html
from django.db.models import Count

# Poll model admin
class PollAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created_at', 'updated_at')  # نمایش فیلدهای انتخاب شده در لیست
    search_fields = ('text',)  # امکان جستجو در متن نظرسنجی
    list_filter = ('created_at',)  # امکان فیلتر کردن بر اساس تاریخ ایجاد
    ordering = ('-created_at',)  # ترتیب نمایش بر اساس تاریخ ایجاد
    readonly_fields = ('created_at', 'updated_at')  # نمایش فقط خواندنی فیلدهای تاریخ

    def created_at(self, obj):
        return obj.created_at
    created_at.admin_order_field = 'created_at'  # این کد به ترتیب‌دهی بر اساس تاریخ کمک می‌کند

    def updated_at(self, obj):
        return obj.updated_at
    updated_at.admin_order_field = 'updated_at'

# Poll_comment model admin
class PollCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'poll', 'created_at')  # نمایش شناسه، نام کاربری، نظر و تاریخ
    search_fields = ('username__username', 'poll__text')  # جستجو در نام کاربری و متن نظرسنجی
    list_filter = ('created_at',)  # فیلتر بر اساس تاریخ ایجاد
    ordering = ('-created_at',)  # مرتب‌سازی بر اساس تاریخ
    readonly_fields = ('created_at',)  # نمایش فقط خواندنی تاریخ ایجاد

# Notification model admin
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('number', 'text', 'created_at')  # نمایش شماره و متن اعلان
    search_fields = ('text',)  # جستجو در متن اعلان
    list_filter = ('created_at',)  # فیلتر بر اساس تاریخ ایجاد
    ordering = ('-created_at',)  # مرتب‌سازی بر اساس تاریخ
    readonly_fields = ('created_at',)  # نمایش فقط خواندنی تاریخ ایجاد

# Notification_User model admin
class NotificationUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'notification', 'is_read', 'created_at')  # نمایش نام کاربری و اعلان
    search_fields = ('username__username', 'notification__text')  # جستجو در نام کاربری و متن اعلان
    list_filter = ('is_read', 'created_at')  # فیلتر بر اساس خوانده شدن و تاریخ ایجاد
    ordering = ('-created_at',)  # مرتب‌سازی بر اساس تاریخ
    readonly_fields = ('created_at',)  # نمایش فقط خواندنی تاریخ ایجاد

    def is_read(self, obj):
        return format_html('<span style="color: {};">{}</span>', 
                           'green' if obj.is_read else 'red', 
                           'خوانده شده' if obj.is_read else 'خوانده نشده')
    is_read.short_description = 'وضعیت خواندن'

    def created_at(self, obj):
        return obj.created_at
    created_at.admin_order_field = 'created_at'


# ثبت مدل‌ها در admin
admin.site.register(Poll, PollAdmin)
admin.site.register(Poll_comment, PollCommentAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Notification_User, NotificationUserAdmin)
"""