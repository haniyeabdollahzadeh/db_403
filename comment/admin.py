from django.contrib import admin
from .models import Poll, Poll_comment, Notification, Notification_User
from django.utils.translation import gettext_lazy as _

# --- Poll Admin ---
class PollAdmin(admin.ModelAdmin):
    list_display = ('poll_number', 'text', 'created_at') 
    search_fields = ('poll_number', 'text')  
    list_filter = ('created_at',) 
    ordering = ('-created_at',)  
    date_hierarchy = 'created_at'  

    def created_at(self, obj):
        return obj.created_at
    created_at.admin_order_field = 'created_at'  

# --- Poll_comment Admin ---
class PollCommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'poll', 'comment_text', 'created_at')  
    search_fields = ('username__username', 'comment_text')  
    list_filter = ('created_at',) 
    ordering = ('-created_at',) 
    date_hierarchy = 'created_at'

    def comment_text(self, obj):
        return obj.text
    comment_text.short_description = _('Comment Text')

# --- Notification Admin ---
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('number', 'text', 'created_at')  
    search_fields = ('number', 'text')  
    list_filter = ('created_at',)  
    ordering = ('-created_at',)  
    date_hierarchy = 'created_at'

    def created_at(self, obj):
        return obj.created_at
    created_at.admin_order_field = 'created_at'

# --- Notification_User Admin ---
class NotificationUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'number', 'read_status', 'created_at')  
    search_fields = ('username__username',)  
    list_filter = ('created_at', 'read_status')  
    ordering = ('-created_at',)  
    date_hierarchy = 'created_at'

    def read_status(self, obj):
        return "خوانده شده" if obj.is_read else "خوانده نشده"
    read_status.short_description = _('Read Status')

admin.site.register(Poll, PollAdmin)
admin.site.register(Poll_comment, PollCommentAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Notification_User, NotificationUserAdmin)
