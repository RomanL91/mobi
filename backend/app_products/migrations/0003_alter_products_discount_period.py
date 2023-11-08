# Generated by Django 4.2.7 on 2023-11-07 09:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='discount_period',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 11, 10, 15, 15, 54, 845009), help_text='По умолчанию +3 дня от времени создания карточки продукта', verbose_name='Действие скидки до'),
        ),
    ]