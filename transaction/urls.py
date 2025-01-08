from django.urls import path
from . import views

urlpatterns = [
    path('transactions/', views.transaction_list, name='transaction-list'),
    path('transactions/<int:transaction_id>/', views.transaction_detail, name='transaction-detail'),
    path('transactions/create/', views.transaction_create, name='transaction-create'),
]
