# Generated by Django 4.2.7 on 2023-11-08 05:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tags', '0002_initial'),
        ('app_products', '0006_alter_products_discount_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='discount_period',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 11, 11, 11, 16, 53, 223237), help_text='По умолчанию +3 дня от времени создания карточки продукта', verbose_name='Действие скидки до'),
        ),
        migrations.AlterField(
            model_name='products',
            name='display_tag',
            field=models.BooleanField(default=False, verbose_name='Показывать ТЕГ'),
        ),
        migrations.AlterField(
            model_name='products',
            name='tag',
            field=models.ManyToManyField(blank=True, to='app_tags.tags', verbose_name='ТЕГ'),
        ),
    ]
