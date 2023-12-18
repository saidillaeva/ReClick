from django.urls import path
from . import views

app_name = 'persons'
urlpatterns = [
    path('person_list/', views.PersonListView.as_view(), name='person_list'),
    path('person_list/<int:id>/', views.PersonDetailView.as_view()),
    path('person_list/<int:id>/delete/', views.PhoneDeleteView.as_view()),
    path('person_list/<int:id>/update/', views.PersonUpdateView.as_view()),
    path('create_person/', views.PersonCreateView.as_view()),
    path("searching/", views.SearchView.as_view(), name="searching"),
]