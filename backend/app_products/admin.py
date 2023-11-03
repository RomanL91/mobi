from django.contrib import admin

from app_products.models import Products, ProductImage


class ProductsAdmin(admin.ModelAdmin):
    pass


class ProductImageAdmin(admin.ModelAdmin):
   pass


class ProductImageInline(admin.StackedInline):
  model = ProductImage
  max_num = 10
  extra = 0


class ProductAdmin(admin.ModelAdmin):
  inlines = [ProductImageInline,]


admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Products, ProductAdmin)
