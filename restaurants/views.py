from django.shortcuts import render, get_object_or_404
from . import models


def RestaurantsListView(request):
    show = models.Restaurant.objects.all()
    context = {
        'show_key': show,

    }
    html_name = 'home_page/banquets.html'
    return render(request, html_name, context)


# def ThingsDetailView(request, id):
#     if  request.method == "GET":
#         show_id_key = get_object_or_404(RestaurantsListView, id=id)
#         return render(request, template_name='things/things_detail.html', context={"show_id_key":show_id_key})

def RestaurantListView(request):
        restaurants = models.Restaurant.objects.filter(type='restaurant')

        context = {'restaurants': restaurants}
        html_name = 'home_page/banquets.html'
        return render(request, html_name, context)


def BanquetsListView(request):
    banquets = models.Restaurant.objects.filter(type='banquet')

    context = {'banquets': banquets}
    html_name = 'home_page/banquets.html'
    return render(request, html_name, context)