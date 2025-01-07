from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .forms import FoodForm
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


