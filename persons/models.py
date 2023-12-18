from django.db import models


class Person(models.Model):
    GENDER = (
        ('M', 'M'),
        ('F', "F"),
    )
    name = models.CharField(max_length=100, verbose_name='Enter your name')
    age = models.PositiveIntegerField(verbose_name='Enter your age')
    hobby = models.TextField(verbose_name='Your Hobby')
    gender = models.CharField(max_length=100, choices=GENDER)
    phone_number = models.CharField(max_length=14, default='+996', verbose_name='Your Number')

    def __str__(self):
        return self.name
