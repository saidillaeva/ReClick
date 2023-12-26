from django.urls import path
from .views import reservation, hall_detail, hall_list

urlpatterns = [
    path('reservation/', reservation, name='reservation'),
    path('halls/', hall_list, name='hall_list'),  # Добавить паттерн URL для отображения всех залов
    path('hall/<int:hall_id>/', hall_detail, name='hall_detail'),
]