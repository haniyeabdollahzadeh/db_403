from django import forms
from .models import Food, Reservation



class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'price']


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['food_name', 'quantity'] 

    meal_type = forms.ChoiceField(

        choices=Food.MEAL_CHOICES,
        label='انتخاب وعده غذایی',
        widget=forms.RadioSelect,
    )     

    def __ini__(seld, *args, **kwargs):
        super().__init__(*args, **kwargs)
        meal_type = self.initial.get('meal_type')
        if meal_type:
            self.fields['food_name'].queryset = Food.objects.filter(meal_type = meal_type)      