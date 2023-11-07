from django.db import models

from datetime import datetime, timedelta

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def valid(value):
    if value < 0:
        raise ValidationError(
                _("%(value)s Не может быть отрицательным"),
                params={"value": value},
            )


class Promo(models.Model):
    name_promo = models.CharField(
        verbose_name='Название ПРОМО', max_length=150, unique=True
    )
    discount_period_promo = models.DateTimeField(
        verbose_name='Действие скидки ПРОМО до', default=datetime.now()+timedelta(days=3), blank=False,
        help_text='По умолчанию +3 дня от времени создания карточки продукта'
    )
    desc_promo = models.TextField(
        verbose_name='Описание ПРОМО', max_length=1500, blank=True
    )
    pass_promo = models.CharField(
        verbose_name='ПРОМО слово/ключ/пароль', max_length=150, unique=True
    )
    discont_promo = models.DecimalField(
        verbose_name='Скидка по ПРОМО', 
        validators=[valid,],
        max_digits=4, decimal_places=2, default=0
    )


    def __str__(self) -> str:
        return f'ПРОМО: {self.name_promo} | КОД: {self.pass_promo} | СКИДКА: {self.discont_promo}'
