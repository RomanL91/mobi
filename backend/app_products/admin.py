from django.contrib import admin

from app_products.models import Products


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    pass
