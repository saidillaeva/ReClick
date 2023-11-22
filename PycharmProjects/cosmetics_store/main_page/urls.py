from django.urls import path
from .views import string_post_view, product_detail_view

urlpatterns = [
    path('home_page/', string_post_view),
    path('product_detail/<int:id>/', product_detail_view),
]