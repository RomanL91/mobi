from django.db import models

from django.core.validators import RegexValidator

from app_products.models import Products


class ColorField(models.CharField):
    """ Поле для хранения HTML-кода цвета."""

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 7)
        super().__init__(*args, **kwargs)
        self.validators.append(RegexValidator(r'#[a-f\d]{6}'))


class Color(models.Model):
    color = ColorField(default='#FF0000', verbose_name='Цвет')
    name_color = models.CharField(
        verbose_name='Название цвета', max_length=35, default='Красный'
    )
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Продукт')


    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    
    def __str__(self) -> str:
        return self.color
