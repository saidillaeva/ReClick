from django.shortcuts import render, get_object_or_404
from .models import RunString, RestaurantPostModel, Afisha, Slider


def string_post_view(request):
    if request.method == 'GET':
        string_ = RunString.objects.all()
        restaurant_list = RestaurantPostModel.objects.all()
        afisha = Afisha.objects.all()
        slider = Slider.objects.all()
        return render(request, template_name='home_page/index.html',
                      context={
                          'string_': string_,
                          'restaurant_list': restaurant_list,
                          'afisha': afisha,
                          'slider_list': slider

                      })


def restaurants_detail_view(request, id):
    if request.method == 'GET':
        restaurant_id = get_object_or_404(RestaurantPostModel, id=id)
        return render(request, template_name='home_page/restaurant_detail.html', context={'restaurant_id': restaurant_id})

