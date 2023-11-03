from django.contrib import admin

from app_promo.models import Promo


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = [
        'name_promo',
        'desc_promo',
        'pass_promo',
        'discont_promo',
    ]
