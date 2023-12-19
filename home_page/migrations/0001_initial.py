# Generated by Django 5.0 on 2023-12-15 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Afisha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_restaurant', models.CharField(max_length=100)),
                ('time_title', models.TimeField()),
                ('place', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantPostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurants', models.CharField(max_length=100, verbose_name='Enter your restaurants name')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='products/')),
                ('cost', models.PositiveIntegerField()),
                ('genre', models.CharField(choices=[('Russian', 'Russian'), ('Italian', 'Italian'), ('American', 'American'), ('Japanese', 'Japanese'), ('Chinese', 'Chinese')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('address', models.TextField()),
                ('contact_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='RunString',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Enter your title')),
                ('description', models.TextField(verbose_name='Enter your description')),
            ],
            options={
                'verbose_name': 'Ticker',
                'verbose_name_plural': 'Tickers',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.URLField()),
            ],
        ),
    ]
