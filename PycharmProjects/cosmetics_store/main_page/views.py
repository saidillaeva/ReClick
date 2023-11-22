from django.shortcuts import render, get_object_or_404
from .models import RunString, ProductPostModel, Afisha, Slider


def string_post_view(request):
    if request.method == 'GET':
        string_ = RunString.objects.all()
        product_list = ProductPostModel.objects.all()
        afisha = Afisha.objects.all()
        slider = Slider.objects.all()
        return render(request, template_name='main_page/index.html',
                      context={
                          'string_': string_,
                          'product_list': product_list,
                          'afisha': afisha,
                          'slider_list': slider

                      })


def product_detail_view(request, id):
    if request.method == 'GET':
        product_id = get_object_or_404(ProductPostModel, id=id)
        return render(request, template_name='main_page/product_detail.html', context={'product_id': product_id})
