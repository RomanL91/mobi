from django.db import models

from app_products.models import Products


class Basket(models.Model):
    user_session = models.CharField(
        verbose_name='Сессия пользователя', max_length=300, editable=True,
    )

    products = models.ForeignKey(
        Products, verbose_name='Продукт',
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(
        verbose_name='Количество продукта', 
        default=0,
    )

    add_datetime = models.DateTimeField(
        verbose_name="Время добавления", auto_now_add=True
    )

    promo_active = models.BooleanField(
        verbose_name='Активировано ПРОМО', default=False
    )


    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


    def __str__(self) -> str:
        return self.products.name_product    


    @property
    def product_cost(self):
        product_cost = self.products.price_with_discount_or_PROMO * self.quantity
        return product_cost
    

    @property
    def total_cost(self):
        _items = Basket.objects.filter(user_session=self.user_session)
        _totalcost = sum(list(map(lambda x: x.product_cost, _items)))
        return _totalcost
    

class Order(models.Model):
    user_session = models.CharField(
        verbose_name='Сессия пользователя', max_length=300, editable=True,
    )

    user_name = models.CharField(
        verbose_name='Имя пользователя', max_length=150,
        blank=True, null=True
    )

    user_telephone = models.CharField(
        verbose_name='Телефонный номер', max_length=20,
        blank=True, null=True
    )

    order_delivery = models.BooleanField(
        verbose_name='Доставка', default=False
    )

    order_delivery_address = models.CharField(
        verbose_name='Адресс доставки', max_length=300,
        blank=True, null=True
    )

    order_total_price = models.DecimalField(
        verbose_name='Общая стоимость заказа', 
        max_digits=10000, decimal_places=2, default=0,
        blank=True, null=True
    )

    promo = models.CharField(
        verbose_name='Примененное промо', max_length=200,
        blank=True, null=True
    )

    creation_date_and_time = models.DateTimeField(
        verbose_name='Дата и время и создания', auto_now=True,
        auto_created=True
    )

    order_product_list = models.JSONField(
        verbose_name='Продукты данного заказа', default=dict,
        blank=True, 
        null=True,
        editable=True
    )


    class Meta:
        verbose_name = 'Ордер'
        verbose_name_plural = 'Ордера'


    def __str__(self) -> str:
        if self.user_telephone != '':
            return self.user_telephone
        return 'Не указан номер телефона'
        