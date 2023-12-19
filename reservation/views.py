from django.shortcuts import render, get_object_or_404
from .models import BanquetHall
from .forms import ReservationForm, ReviewForm
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


def hall_detail(request, hall_id):
    hall = get_object_or_404(BanquetHall, pk=hall_id)
    reviews = hall.reviews.all()  # Получаем все отзывы для этого банкетного зала

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.hall = hall
            new_review.save()

            # Обновляем рейтинг банкетного зала на основе нового отзыва
            hall.total_reviews += 1
            hall.rating = (hall.rating * (hall.total_reviews - 1) + new_review.rating) / hall.total_reviews
            hall.save()

            return render(request, 'hall_detail.html', {'hall': hall, 'reviews': reviews, 'review_form': ReviewForm()})
    else:
        review_form = ReviewForm()

    # Убедитесь, что в конце представления возвращается объект HttpResponse
    return render(request, 'hall_detail.html', {'hall': hall, 'reviews': reviews, 'review_form': review_form})