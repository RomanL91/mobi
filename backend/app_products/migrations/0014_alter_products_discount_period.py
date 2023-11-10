# Generated by Django 4.2.7 on 2023-11-09 07:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0013_alter_products_discount_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='discount_period',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 11, 12, 13, 30, 28, 438141), help_text='По умолчанию +3 дня от времени создания карточки продукта', verbose_name='Действие скидки до'),
        ),
    ]
