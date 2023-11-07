from django.contrib import admin

from app_basket.models import Basket


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = [
        'user_session',
        'products',
        'quantity',
        'add_datetime',
    ]

    def save_model(self, request, obj, form, change):
       obj.user_session = request.session.__dict__["_SessionBase__session_key"]
       obj.save()
