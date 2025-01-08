from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .forms import FoodForm, ReservationForm



from django.db import connection

@csrf_protect
def food_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')  # فرض می‌کنیم فرم فیلدی به نام name دارد
        description = request.POST.get('description')  # فرض می‌کنیم فرم فیلدی به نام description دارد
        price = request.POST.get('price')  # فرض می‌کنیم فرم فیلدی به نام price دارد
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO reservation_food (name, description, price) VALUES (%s, %s, %s)",
                [name, description, price]
            )
        return redirect('food_list')
    return render(request, 'food_create.html')


from django.db import connection


def food_list(request):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM reservation_food"
        )  # در اینجا 'reservation_food' نام جدول Food است
        foods = cursor.fetchall()
    return render(request, "food_list.html", {"foods": foods})


from django.db import connection


@login_required
def reservation_create(request):
    if request.method == "POST":
        food_id = request.POST.get("food")  # فرض می‌کنیم فرم فیلدی به نام food دارد
        quantity = request.POST.get(
            "quantity"
        )  # فرض می‌کنیم فرم فیلدی به نام quantity دارد
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO reservation_reservation (user_id, food_id, quantity) VALUES (%s, %s, %s)",
                [request.user.id, food_id, quantity],
            )
        return HttpResponse("رزرو شما با موفقیت ثبت شد!")
    return render(request, "reservation_create.html", {"form": ReservationForm()})


from django.db import connection


@login_required
def reservation_create(request):
    if request.method == "POST":
        food_id = request.POST.get("food")  # فرض می‌کنیم فرم فیلدی به نام food دارد
        quantity = request.POST.get(
            "quantity"
        )  # فرض می‌کنیم فرم فیلدی به نام quantity دارد
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO reservation_reservation (user_id, food_id, quantity) VALUES (%s, %s, %s)",
                [request.user.id, food_id, quantity],
            )
        return HttpResponse("رزرو شما با موفقیت ثبت شد!")
    return render(request, "reservation_create.html", {"form": ReservationForm()})


from django.db import connection
from django.shortcuts import render


@login_required
def reservation_list(request):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT r.id, u.username, f.name, r.quantity, (r.quantity * f.price) AS total_price, r.created_at
            FROM reservation_reservation r
            JOIN reservation_food f ON r.food_id = f.id
            JOIN auth_user u ON r.user_id = u.id
        """
        )
        reservations = cursor.fetchall()

    return render(request, "reservation_list.html", {"reservations": reservations})
