from django.db import models


class RunString(models.Model):
    title = models.CharField(max_length=100, verbose_name='Enter your title')
    description = models.TextField(verbose_name='Enter your description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ticker'
        verbose_name_plural = 'Tickers'


class ProductPostModel(models.Model):
    GENRE = (
        ('Adults', 'Adults'),
        ('Babies', 'Babies')
    )
    title = models.CharField(max_length=100, verbose_name="Enter your product name")
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    cost = models.PositiveIntegerField()
    genre = models.CharField(max_length=100, choices=GENRE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Afisha(models.Model):
    title_product = models.CharField(max_length=100, null=True)
    time_title = models.TimeField()
    place = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.title_product

class Slider(models.Model):
    photo = models.URLField()

    def __str__(self):
        return self.photo
