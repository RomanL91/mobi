from django.db import models


class Products(models.Model):
    # категория - одна

    # photo = photo - много
    # color = color - один

    name_product = models.CharField(verbose_name='Наименование продукта', max_length=150)
    desc_product = models.TextField(verbose_name='Описание продукта', max_length=1000, blank=True)


    display_price = models.BooleanField(verbose_name='Отображать цену', default=False)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2, blank=True)

    display_discount = models.BooleanField(verbose_name='Отобразить скидку', default=False)
    discount = models.DecimalField(verbose_name='Скидка', max_digits=2, decimal_places=2, blank=True)
    # период действия скидки - отдельной сущностью со связью?

    display_remaining_goods = models.BooleanField(verbose_name='Отобразить остаток товара', default=False)
    remaining_goods = models.BigIntegerField(verbose_name='Остаток товара', default=0, blank=True)

    # показывать теги
    # теги - много
    
    # показывать промо 
    # промо - один

    # показывать рейтинг 
    # рейтингн - много

    # показывать отзывы
    # отзывы - много
    
    # показывать характеристики 
    # характеристики - много

    # слаг поле для индексации предзаполнение с имени
