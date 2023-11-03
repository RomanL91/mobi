from django.contrib import admin

from app_tags.models import Tags


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = [
        'name_tag',
        'desc_tag',
    ]
