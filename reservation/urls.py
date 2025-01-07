from django.urls import path
from . import views

urlpatterns = [
    path('food/create/', views.food_creat, name='food_create'),
    path('foods/', views.food_list, name='food_list'),
]
