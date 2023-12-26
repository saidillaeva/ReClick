from django.shortcuts import get_object_or_404,  redirect
from django.contrib import messages
from .forms import ReservationForm, ReviewForm
from decimal import Decimal

from django.shortcuts import render
from .models import BanquetHall

def hall_list(request):
    halls = BanquetHall.objects.all()
    return render(request, 'hall_list.html', {'halls': halls})


def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():

            return render(request, 'success_page.html')  # Замените 'success_page.html' на ваш шаблон успешного бронирования
    else:
        form = ReservationForm()

    halls = BanquetHall.objects.all()
    return render(request, 'reservation_page.html', {'form': form, 'halls': halls})


def hall_detail(request, hall_id):
    hall = get_object_or_404(BanquetHall, pk=hall_id)
    reviews = hall.reviews.all()

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.hall = hall
            new_review.save()

            # Обновляем рейтинг банкетного зала на основе нового отзыва
            all_reviews = hall.reviews.all()
            total_reviews = len(all_reviews)
            total_rating = sum(review.rating for review in all_reviews)

            hall.rating = Decimal(total_rating) / Decimal(total_reviews)
            hall.save()

            messages.success(request, 'Отзыв успешно отправлен!')
            return redirect('hall_detail', hall_id=hall_id)
    else:
        review_form = ReviewForm()

    return render(request, 'hall_detail.html', {'hall': hall, 'reviews': reviews, 'review_form': review_form})