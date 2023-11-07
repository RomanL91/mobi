from django.db import models

from app_products.models import Products


class Basket(models.Model):
    user_session = models.CharField(
        verbose_name='Сессия пользователя', max_length=300, 
        blank=True, null=True, editable=False
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
    