from django.db import models
from django.db import models

class BanquetHall(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    average_price_per_person = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name
