# Generated by Django 4.2.7 on 2023-11-07 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0003_alter_products_discount_period'),
        ('app_basket', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='total_cost_pos',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Итоговая цена со скидками/ПРОМО'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_products.products', verbose_name='Продукт'),
        ),
    ]