from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.signup, name='signup'),# مسیر ثبت‌نام
      path('login/', views.custom_login, name='login'),  
    
]

