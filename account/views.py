from django.db import connection
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password  # برای هش کردن رمز عبور
from django.contrib.auth import login
from django.contrib.auth.hashers import check_password


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get(
            "password1"
        )  # فرض می‌کنیم رمز در فیلد `password1` باشه
        email = request.POST.get("email")
        phone = request.POST.get("phone", None)  # فیلد اختیاری
        access_level = request.POST.get("access_level", "U")  # پیش‌فرض: "user"

        if username and password and email:  # اعتبارسنجی اولیه
            hashed_password = make_password(password)  # هش کردن رمز عبور

            # اجرای کوئری INSERT
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO account_user (username, password, email, is_active, date_joined, first_name, last_name)
                    VALUES (%s, %s, %s, %s, NOW(), %s, %s)
                    """,
                    [username, hashed_password, email, 1, "", ""],  # مقادیر لازم
                )

                # گرفتن user_id برای درج اطلاعات اضافی (مثل phone و access_level)
                user_id = cursor.lastrowid
                cursor.execute(
                    """
                    INSERT INTO account_user (user_ptr_id, phone, access_level, credit, created_at)
                    VALUES (%s, %s, %s, %s, NOW())
                    """,
                    [user_id, phone, access_level, 0.0],  # مقدار پیش‌فرض credit: 0.0
                )

            messages.success(request, "حساب کاربری شما با موفقیت ایجاد شد!")
            return redirect("login")
        else:
            messages.error(request, "لطفاً فرم را به درستی پر کنید.")

    return render(request, "registration/signup.html")


def custom_login(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id, password
                    FROM auth_user
                    WHERE username = %s AND is_active = 1
                    """,
                    [username],
                )
                user = cursor.fetchone()

            if user:
                user_id, hashed_password = user
                if check_password(password, hashed_password):  # بررسی رمز عبور
                    # اگر رمز عبور درست باشد، کاربر را لاگین می‌کنیم
                    from django.contrib.auth.models import User

                    user_instance = User.objects.get(
                        pk=user_id
                    )  # گرفتن نمونه کاربر از مدل
                    login(request, user_instance)

                    next_url = request.GET.get("next", "home")
                    return redirect(next_url)
                else:
                    messages.error(request, "نام کاربری یا رمز عبور اشتباه است.")
            else:
                messages.error(request, "نام کاربری یا رمز عبور اشتباه است.")
        else:
            messages.error(request, "لطفاً فرم را به درستی پر کنید.")

    return render(request, "registration/login.html")
