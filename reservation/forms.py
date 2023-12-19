from django import forms
from .models import BanquetHall, Review

class ReservationForm(forms.Form):
    hall = forms.ModelChoiceField(queryset=BanquetHall.objects.all(), empty_label="Select a hall")
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    guests = forms.IntegerField(min_value=1, label='Number of Guests')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'rating', 'comment']