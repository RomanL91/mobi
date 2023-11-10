from django.contrib import admin

from django import forms

from app_color.models import Color, ColorField


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = [
        'name_color', 
        'color'
    ]
    formfield_overrides = {
        ColorField: {'widget': forms.TextInput(attrs={'type': 'color'})}
    }
