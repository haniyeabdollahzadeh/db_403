from django import forms
from .models import Food
from django.views.decorators.csrf import csrf_protect


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'price']