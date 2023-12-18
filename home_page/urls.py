from django.urls import path
from .views import string_post_view, restaurants_detail_view

app_name='home_page'
urlpatterns = [
    path('home_page/', string_post_view, name='home_page'),
    path('restaurant_detail/<int:id>/', restaurants_detail_view),
]