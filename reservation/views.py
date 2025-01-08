from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .forms import FoodForm, ReservationForm
from .models import Food, Reservation

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


@login_required
def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservation_list.html', {'reservations': reservations})



