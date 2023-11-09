# Generated by Django 4.2.7 on 2023-11-09 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_basket', '0008_alter_basket_user_session'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='basket',
            constraint=models.UniqueConstraint(fields=('user_session', 'products'), name='app_basket_basket_user_session_products'),
        ),
    ]
