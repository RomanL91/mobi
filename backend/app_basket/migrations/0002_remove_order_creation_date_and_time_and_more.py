# Generated by Django 4.2.7 on 2023-12-11 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_basket', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='creation_date_and_time',
        ),
        migrations.RemoveField(
            model_name='order',
            name='promo',
        ),
    ]
