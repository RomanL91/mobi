# Generated by Django 4.2.7 on 2023-11-06 09:38

import app_products.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0005_alter_products_display_reviews_alter_products_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price_with_discount_or_PROMO',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, validators=[app_products.models.valid], verbose_name='Итоговая цена со скидками/ПРОМО'),
        ),
        migrations.AlterField(
            model_name='products',
            name='display_discount',
            field=models.BooleanField(default=False, verbose_name='Отобразить/Применить скидку'),
        ),
    ]
