from django.urls import path
from .views import string_post_view, restaurants_detail_view

urlpatterns = [
    path('home_page/', string_post_view),
    path('restaurant_detail/<int:id>/', restaurants_detail_view),
]