# Generated by Django 4.2.7 on 2023-11-03 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0006_productimage_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(blank=True, upload_to='product_images/%Y/%m/%d/%H/%M/%S/', verbose_name='Изображение'),
        ),
    ]
