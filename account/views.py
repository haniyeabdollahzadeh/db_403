from django.db import connection
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password  # برای هش کردن رمز عبور

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        email = request.POST.get('email')

        if username and password and email:
            hashed_password = make_password(password)  # هش کردن رمز عبور
            with connection.cursor() as cursor:
                try:
                    cursor.execute("""
                        INSERT INTO account_user (username, password, email, is_active, date_joined)
                        VALUES (%s, %s, %s, %s, NOW())
                    """, [username, hashed_password, email, True])  # مقدار is_active = True
                    messages.success(request, 'حساب کاربری شما با موفقیت ایجاد شد!')
                    return redirect('login')
                except Exception as e:
                    messages.error(request, 'خطا در ایجاد حساب کاربری: {}'.format(e))
        else:
            messages.error(request, 'لطفاً همه فیلدها را پر کنید.')

    return render(request, 'registration/signup.html')


def custom_login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id, username, password FROM account_user 
                    WHERE username = %s AND is_active = TRUE
                """, [username])
                user = cursor.fetchone()

                if user:
                    user_id, db_username, db_password = user
                    if check_password(password, db_password):  
                        from account.models import User 
                        user = User.objects.get(pk=user_id)
                        login(request, user)
                        next_url = request.GET.get('next', 'home')
                        return redirect(next_url)
                    else:
                        messages.error(request, "رمز عبور اشتباه است.")
                else:
                    messages.error(request, "کاربری با این مشخصات یافت نشد.")
        else:
            messages.error(request, "لطفاً همه فیلدها را پر کنید.")

    return render(request, 'registration/login.html')
