from django.db import models

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from app_category.models import Category
from app_tags.models import Tags
from app_promo.models import Promo
from app_color.models import Color

from datetime import datetime, timedelta


def valid(value):
    if value < 0:
        raise ValidationError(
                _("%(value)s Не может быть отрицательным"),
                params={"value": value},
            )
    

def rating_valid(value):
    if not 5 >= float(value) >= 0:
        raise ValidationError(
                _("%(value)s Оценка может быть от 0 до 5"),
                params={"value": value},
            )


class Products(models.Model):
    # ================= Категории
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Категория продукта'
    )
    # ================= Имя, Описание
    name_product = models.CharField(verbose_name='Наименование продукта', max_length=150)
    color = models.ForeignKey(
        Color, on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name='Цвет')
    desc_product = models.TextField(verbose_name='Описание продукта', max_length=1000, blank=True)
    # ================= Все связанное с ценой продукта
    display_price = models.BooleanField(verbose_name='Отображать цену', default=False)
    price = models.DecimalField(
        verbose_name='Цена', 
        validators=[valid,],
        max_digits=15, decimal_places=2, default=0, 
        blank=True, null=True
    )
    price_with_discount_or_PROMO = models.DecimalField(
        verbose_name='Итоговая цена со скидками/ПРОМО', 
        validators=[valid,],
        max_digits=15, decimal_places=2, default=0, 
        blank=True, null=True
    )
    # ================= Все связанное с акцией на продукт
    display_discount = models.BooleanField(verbose_name='Отобразить/Применить скидку', default=False)
    discount = models.DecimalField(
        verbose_name='Скидка', 
        validators=[valid,],
        max_digits=4, decimal_places=2, default=0, 
        blank=True, null=True
    )
    discount_period = models.DateTimeField(
        verbose_name='Действие скидки до', default=datetime.now()+timedelta(days=3), blank=True,
        help_text='По умолчанию +3 дня от времени создания карточки продукта'
    )
    # ================= Остаток продукта
    display_remaining_goods = models.BooleanField(verbose_name='Отобразить остаток товара', default=False)
    remaining_goods = models.PositiveIntegerField(verbose_name='Остаток товара', default=0, blank=True)
    # ================= ТЭГИ для продукта
    display_tag = models.BooleanField(verbose_name='Показывать ТЕГ', default=False)
    tag = models.ManyToManyField(Tags, verbose_name='ТЕГ', blank=True)
    # ================= ПРОМО на продукт
    display_promo = models.BooleanField(verbose_name='Отобразить/Применить ПРОМО', default=False)
    promo = models.ForeignKey(
        Promo, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Участие продукта в промо'
    )
    # ================= Отзывы и рейтинг продукта
    display_reviews = models.BooleanField(verbose_name='Отображать отзывы/Рейтинг', default=False)
    rating = models.DecimalField(
        verbose_name='Рейтинг',
        validators=[rating_valid,],
        max_digits=4, decimal_places=1, default=0,
        blank=True, null=True
    )
    
    # показывать характеристики 
    # характеристики - много

    # слаг поле для индексации предзаполнение с имени

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


    def __str__(self) -> str:
        return self.name_product


class ProductImage(models.Model):
    image = models.ImageField(verbose_name='Изображение', blank=True, upload_to='product_images/%Y/%m/%d/%H/%M/%S/')
    desc = models.TextField(verbose_name='Описание', max_length=1500, blank=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Продукт')

    class Meta:
            verbose_name = 'Изображение'
            verbose_name_plural = 'Изображения'


    def __str__(self) -> str:
        return self.product.name_product
