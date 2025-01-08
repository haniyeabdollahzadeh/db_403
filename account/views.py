from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from account.forms import CustomUserCreationForm

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
