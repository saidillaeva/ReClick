from django.db import models


class RunString(models.Model):
    title = models.CharField(max_length=100, verbose_name='Enter your title')
    description = models.TextField(verbose_name='Enter your description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ticker'
        verbose_name_plural = 'Tickers'


class RestaurantPostModel(models.Model):
    GENRE = (
        ('Russian', 'Russian'),
        ('Italian', 'Italian'),
        ('American', 'American'),
        ('Japanese', 'Japanese'),
        ('Chinese', 'Chinese'),

    )
    restaurant = models.CharField(max_length=100, verbose_name="Enter your restaurants name")
    description = models.TextField()
    image = models.ImageField(upload_to='restaurants/')
    cost = models.PositiveIntegerField()
    genre = models.CharField(max_length=100, choices=GENRE)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.restaurant


class Afisha(models.Model):
    title_restaurant = models.CharField(max_length=100)
    time_title = models.TimeField()
    place = models.CharField(max_length=10)

    def __str__(self):
        return self.title_restaurant

class Slider(models.Model):
    photo = models.URLField()

    def __str__(self):
        return self.photo

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    cuisine = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "restaurants"

    def __str__(self):
        return self.name
