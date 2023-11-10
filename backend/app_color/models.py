from django.db import models

from django.core.validators import RegexValidator


class ColorField(models.CharField):
    """ Поле для хранения HTML-кода цвета."""

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 7)
        super().__init__(*args, **kwargs)
        self.validators.append(RegexValidator(r'#[a-f\d]{6}'))


class Color(models.Model):
    color = ColorField(unique=True, default='#FF0000', verbose_name='Цвет')
    name_color = models.CharField(
        unique=True,
        verbose_name='Название цвета', max_length=35, default='Красный'
    )


    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    
    def __str__(self) -> str:
        return self.name_color
    
