# Generated by Django 5.0 on 2023-12-19 19:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banquethall',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='banquethall',
            name='total_reviews',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='reservation.banquethall')),
            ],
        ),
    ]