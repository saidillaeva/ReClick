from django.urls import path
from .views import string_post_view, restaurants_detail_view, SearchResultsView, HomePageView


app_name = 'home_page'
urlpatterns = [
    path('home_page/', string_post_view, name='home_page'),
    path('restaurant_detail/<int:id>/', restaurants_detail_view),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('header/', HomePageView.as_view(), name='header'),
]