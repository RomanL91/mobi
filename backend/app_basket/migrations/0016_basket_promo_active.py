# Generated by Django 4.2.7 on 2023-11-28 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_basket', '0015_remove_basket_app_basket_basket_user_session_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='promo_active',
            field=models.BooleanField(default=False, verbose_name='Активировано ПРОМО'),
        ),
    ]