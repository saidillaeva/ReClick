from django.db import models

class TvShow(models.Model):
    CHOICE_ACTUALITY =(
        ('ДА', "ДА"),
        ('НЕТ', "НЕТ")
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='film/')
    act = models.CharField(max_length=100, choices=CHOICE_ACTUALITY)
    cost = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title