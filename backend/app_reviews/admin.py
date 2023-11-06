from django.contrib import admin

from app_reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        'phone_number', 'rating', 'review', 'moderation', 'product',
    ]