from django.urls import path
from .views import reservation, hall_detail

urlpatterns = [
    path('reservation/', reservation, name='reservation'),
    path('hall/<int:hall_id>/', hall_detail, name='hall_detail')
]