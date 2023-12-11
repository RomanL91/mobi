import json

from django.db import models
from django.contrib import admin

from app_basket.models import Basket, Order
from app_products.models import Products

from django_json_widget.widgets import JSONEditorWidget # ЕСТЬ И ГОТОВЫЕ РЕШЕНИЯ для JSON
from django.contrib.admin.widgets import AdminTextareaWidget
from django.utils.html import format_html


class CustomAdminJSONWidget(AdminTextareaWidget):
    def render(self, name, value, attrs=None, renderer=None):
        result = []
        if name == 'order_product_list':
            value_list = json.loads(value)
            for el  in value_list:
                p, q, t, pr = el.values()
                result.extend(
                    f'''
                    Продукт: {p}\n\t\r<br>
                    Колличество: {q}\n\t\r<br>
                    Время добаления в корзину: {t}\n\t\r<br>
                    Приминение ПРОМО: {pr}\n\t\r<br>
                    {'='*80}\n\t\r<br>
                    '''
                )
        return format_html("".join(result))


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = [
        'user_session',
        'products',
        'quantity',
        'add_datetime',
    ]


    def save_model(self, request, obj, form, change):
        if change:
            obj.quantity=int(form.data['quantity'])
        else:
            obj = Basket.objects.get_or_create(
                user_session=form.data['user_session'], 
                products=Products.objects.get(pk=form.data['products']),
            )
            obj, flag = obj
            obj.quantity=int(form.data['quantity'])

        obj.save()


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user_session',
        'user_name',
        'user_telephone',
        'order_delivery',
        'order_delivery_address',
        'promo',
        'creation_date_and_time',
        'get_list_products',

    ]
    formfield_overrides = {
        models.JSONField: {'widget': CustomAdminJSONWidget}, # Или сделать кастомный виджет ЕСТЬ И ГОТОВЫЕ РЕШЕНИЯ
    }


    def get_list_products(self, obj):
        result = []
        for el in obj.order_product_list:
            p, q, t, pr = el.values()
            result.extend(
                    f'''
                    Продукт: {p}<br>
                    Колличество: {q}<br>
                    Время добаления в корзину: {t}<br>
                    Приминение ПРОМО: {pr}<br>
                    {'='*80}\n\t\r<br>
                    '''
                )
        return format_html("".join(result))
    get_list_products.short_description = 'Список продуктов заказа'
