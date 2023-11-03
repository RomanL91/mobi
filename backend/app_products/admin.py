from django.contrib import admin
from django.utils.html import mark_safe

from app_products.models import Products, ProductImage


class ProductsAdmin(admin.ModelAdmin):
    pass


class ProductImageAdmin(admin.ModelAdmin):
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="600" ')


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    max_num = 10
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline,]


admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Products, ProductAdmin)
