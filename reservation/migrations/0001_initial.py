# Generated by Django 5.0 on 2023-12-19 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BanquetHall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('capacity', models.IntegerField()),
                ('average_price_per_person', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.TextField()),
            ],
        ),
    ]
