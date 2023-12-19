from django.shortcuts import render
from .models import BanquetHall
from .forms import ReservationForm
def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Обработка бронирования здесь
            # Можете сохранить бронь в базу данных или отправить уведомление
            return render(request, 'success_page.html')  # Замените 'success_page.html' на ваш шаблон успешного бронирования
    else:
        form = ReservationForm()

    halls = BanquetHall.objects.all()
    return render(request, 'reservation_page.html', {'form': form, 'halls': halls})
