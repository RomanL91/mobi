from django.contrib import admin

from decimal import Decimal

from app_reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        'phone_number', 'rating', 'review', 'moderation', 'product',
    ]

    def save_model(self, request, obj, form, change):
        all_reviews_prod = Review.objects.filter(product=obj.product_id)
        olny_rating_prod = [
            el.rating for el in all_reviews_prod if el.moderation
        ]

        if 'moderation' in form.data:
            olny_rating_prod.append(Decimal(form.data['rating']))
            arithmetic_mean = sum(olny_rating_prod) / len(olny_rating_prod)
            obj.product.rating = arithmetic_mean
        else:
            try:
                olny_rating_prod.remove(obj.rating)
                arithmetic_mean = sum(olny_rating_prod) / len(olny_rating_prod)
                obj.product.rating = arithmetic_mean
            except ZeroDivisionError:
                pass
            except ValueError:
                pass

        obj.product.save()
        obj.save()
        