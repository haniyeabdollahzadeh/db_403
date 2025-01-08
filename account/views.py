from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from account.forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

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
