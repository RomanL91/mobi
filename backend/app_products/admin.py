from django.db import models
from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.html import format_html
# from django.template.loader import get_template
from django.contrib.admin.widgets import AdminFileWidget

# from fieldsets_with_inlines import FieldsetsInlineMixin

from app_products.models import Products, ProductImage
from app_reviews.models import Review


class CustomAdminFileWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        result = []
        if hasattr(value, "url"):
            result.append(
                f'''<a href="{value.url}" target="_blank">
                      <img 
                        src="{value.url}" alt="{value}" 
                        width="100" height="100"
                        style="object-fit: cover;"
                      />
                    </a>'''
            )
        result.append(super().render(name, value, attrs, renderer))
        return format_html("".join(result))


class ProductImageAdmin(admin.ModelAdmin):
    readonly_fields = ["preview"]
    list_display = [
        'get_image',
        'product',
        'desc'
    ]

    def preview(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="600" ')
    preview.short_description = 'Предпоказ'

    
    def get_image(self, obj):
        try:
            url_prod = obj.image.url
            return mark_safe(f'<img src={url_prod} width="75"')
        except:
            return None
    get_image.short_description = 'ФОТО'


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    max_num = 10
    extra = 0
    formfield_overrides = {
        models.ImageField: {'widget': CustomAdminFileWidget}
    }
    classes = ['collapse']


class ProductReviewInline(admin.StackedInline):
    model = Review
    extra = 0
    classes = ['collapse']


class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        ('О продукте', {'fields': (('name_product', 'desc_product'),)}),
        ('Остаток продукта', {'fields': (('remaining_goods', 'display_remaining_goods'),), 'classes':('collapse',)}),
        ('Категория', {'fields': (('category',),), 'classes':('collapse',)}),
        ('ТЭГИ', {'fields': (('tag', 'display_tag'),), 'classes':('collapse',)}),
        ('Цена', {'fields': (('price', 'display_price'),), 'classes':('collapse',)}),
        ('Акция', {'fields': (('discount', 'display_discount'),), 'classes':('collapse',)}),
        ('ПРОМО', {'fields': (('promo', 'display_promo'),), 'classes':('collapse',)}),
    )
    filter_horizontal = ['tag',]
    inlines = [ProductImageInline, ProductReviewInline]
    list_display = [
        'get_image',
        'name_product',
        'category',
        'display_price',
        'price',
        'display_discount',
        'discount',
        'display_remaining_goods',
        'remaining_goods',
    ]


    def get_image(self, obj):
        try:
            url_prod = obj.productimage_set.all()[0].image.url
            return mark_safe(f'<img src={url_prod} width="75"')
        except:
            return None
    get_image.short_description = 'ФОТО'


admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Products, ProductAdmin)
