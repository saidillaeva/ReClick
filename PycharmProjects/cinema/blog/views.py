from django.shortcuts import render
from . import models
def post_view(request):
    post_value = models.Post.objects.all()
    return render(request, 'post.html', {'post_key': post_value})
