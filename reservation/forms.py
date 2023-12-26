from django import forms
from .models import BanquetHall, Review

from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        # Проверка на корректность времени (пример)
        if start_time and end_time and start_time >= end_time:
            raise forms.ValidationError("End time should be later than start time")

        return cleaned_data

    def save(self, commit=True):
        reservation = super(ReservationForm, self).save(commit=False)

        # Дополнительные операции, если необходимо

        if commit:
            reservation.save()
        return reservation
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'rating', 'comment']