from django.db import models


class Person(models.Model):
    GENRE = (
        ('Russian', 'Russian'),
        ('Italian', 'Italian'),
        ('American', 'American'),
        ('Japanese', 'Japanese'),
        ('Chinese', 'Chinese'),

    )
    name = models.CharField(max_length=100, verbose_name="Enter your restaurants name", null=True)
    description = models.TextField(null=True)
    average_cost = models.PositiveIntegerField(null=True)
    genre = models.CharField(max_length=100, choices=GENRE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    address = models.TextField(null=True)
    contact_number = models.CharField(max_length=15,null=True)
    phone_number = models.CharField(max_length=14, default='+996', verbose_name='Your Number')

    def __str__(self):
        return self.name

