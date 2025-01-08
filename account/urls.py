from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.signup, name='signup'),# مسیر ثبت‌نام
      path('custom-login/', views.custom_login, name='custom_login'),  
    
]

