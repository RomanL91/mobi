# Generated by Django 4.2.7 on 2023-11-03 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0005_alter_products_discount_alter_products_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='desc',
            field=models.TextField(blank=True, max_length=1500, verbose_name='Описание'),
        ),
    ]
