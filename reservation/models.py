from django.db import models

class BanquetHall(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    average_price_per_person = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()

    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    total_reviews = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.name

class Review(models.Model):
    hall = models.ForeignKey(BanquetHall, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.hall.name}"

from django.db import models
from .models import BanquetHall

class Reservation(models.Model):
    hall = models.ForeignKey(BanquetHall, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    guests = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.hall.name} - {self.date} {self.start_time}-{self.end_time}"