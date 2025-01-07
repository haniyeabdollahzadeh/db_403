from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('food/create/', views.food_creat, name='food_create'),
    path('foods/', views.food_list, name='food_list'),
    path('food/reserve/', views.reservation_create, name='reservation_create'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]
