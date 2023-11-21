from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    cost = models.PositiveIntegerField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

