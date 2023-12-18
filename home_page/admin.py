from django.contrib import admin
from .models import RunString, RestaurantPostModel, Afisha, Slider, Restaurant

admin.site.register(RunString)
admin.site.register(RestaurantPostModel)
admin.site.register(Afisha)
admin.site.register(Slider)

class RestaurantsAdmin(admin.ModelAdmin):
    list_display = ("name", "cuisine",)

admin.site.register(Restaurant, RestaurantsAdmin)
