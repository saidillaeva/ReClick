from django.urls import path
from .views import BanquetsListView
from . import views

urlpatterns = [
    path('banquets/', BanquetsListView, name="banquets")

    # path('', HomePageView.as_view(), name='header'),
]