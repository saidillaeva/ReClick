from django.urls import path
from . import views

urlpatterns = [
    path('', views.tvShowListView),
    path('show_detail/<int:id>/', views.tvShowDetailView),
    path('create_film/', views.createShowView),
    path('delete_list/', views.deleteListView),
    path('delete_list/<int:id>/delete/', views.dropFilmView),
    path('update_list/', views.updateListView),
    path('update_list/<int:id>/update/', views.editFilmView),
]