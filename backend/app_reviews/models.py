from django.db import models

from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from app_products.models import Products


def valid(value):
    if not 5 >= float(value) >= 0:
        raise ValidationError(
                _("%(value)s Оценка может быть от 0 до 5"),
                params={"value": value},
            )


class Review(models.Model):
    phone_number_regex = RegexValidator(regex = r"^\+7\d{10}$")

    rating = models.DecimalField(
        verbose_name='Оценка/Рейтинг',
        validators=[valid,],
        max_digits=2, decimal_places=1, default=5
    )
    review = models.TextField(
        verbose_name='Отзыв', max_length=2000, unique=True
    )
    moderation = models.BooleanField(
        verbose_name='Модерация', default=False
    )
    phone_number = models.CharField(
        verbose_name='Телефонный номер',
        validators=[phone_number_regex,], max_length=12, 
    )
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE, 
        verbose_name='Продукт'
    )


    def __str__(self) -> str:
        return self.product.name_product

