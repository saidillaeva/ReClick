from django.contrib import admin

from django.contrib import admin
from .models import BanquetHall

@admin.register(BanquetHall)
class BanquetHallAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'average_price_per_person', 'description')
    search_fields = ('name', 'description')