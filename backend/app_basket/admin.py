from django.contrib import admin

from app_basket.models import Basket
from app_products.models import Products


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
