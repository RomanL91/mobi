from django.db import models
from django.contrib import admin

from app_basket.models import Basket, Order
from app_products.models import Products

from django_json_widget.widgets import JSONEditorWidget


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
        'order_product_list'
    ]
    # formfield_overrides = {
    #     models.JSONField: {'widget': JSONEditorWidget}, # Или сделать кастомный виджет
    # }
