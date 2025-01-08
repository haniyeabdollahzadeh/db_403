from django.urls import path
from . import views

urlpatterns = [
    path('polls/', views.poll_list, name='poll-list'),  # لیست نظرسنجی‌ها
    path('polls/<int:poll_id>/', views.poll_detail, name='poll-detail'),  # جزئیات یک نظرسنجی خاص
    path('polls/create/', views.poll_created, name='poll-create'),  # ایجاد نظرسنجی جدید
    path('polls/<int:poll_id>/delete/', views.poll_delete, name='poll-delete'),  # حذف نظرسنجی خاص
]
