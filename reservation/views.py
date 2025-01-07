from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm
from account.forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .forms import FoodForm, ReservationForm
from .models import Food

@csrf_protect
def food_creat(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodForm()
        return render(request, 'food_create.html', {'form' : form})
        

def food_list(request):
    foods = Food.objects.all()
    return render(request, 'food_list.html', {'foods' : foods})

@login_required
def reservation_create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # رزرو غذا
            reservation = form.save(commit=False)
            reservation.user = request.user  # فرض بر اینکه کاربر در حال حاضر لاگین است
            reservation.save()
            return HttpResponse('رزرو شما با موفقیت ثبت شد!')
    else:
        form = ReservationForm()

    return render(request, 'reservation_create.html', {'form': form})



def custom_login(request):
    # اگر کاربر در حال حاضر وارد شده باشد، به صفحه اصلی هدایت شود
    if request.user.is_authenticated:
        return redirect('home')  # به صفحه‌ای که می‌خواهید هدایت کنید

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # اعتبارسنجی نام کاربری و رمز عبور
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # لاگین کردن کاربر
                login(request, user)
                
                # پس از لاگین، کاربر به صفحه‌ای که در حال حاضر در آن است یا صفحه‌ای که در URL آمده (پارامتر next) هدایت می‌شود
                next_url = request.GET.get('next', 'home')  # به مسیر 'home' به عنوان پیش‌فرض
                return redirect(next_url)
            else:
                # اگر کاربر نامعتبر باشد، پیامی نشان داده می‌شود
                messages.error(request, "نام کاربری یا رمز عبور اشتباه است.")
        else:
            # اگر فرم معتبر نباشد، ارورهایی نمایش داده می‌شود
            messages.error(request, "لطفاً فرم را به درستی پر کنید.")
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # ثبت‌نام کاربر
            messages.success(request, 'حساب کاربری شما با موفقیت ایجاد شد!')
            return redirect('login')  # بعد از ثبت‌نام به صفحه لاگین هدایت می‌شود
        else:
            messages.error(request, 'لطفاً فرم را به درستی پر کنید.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})