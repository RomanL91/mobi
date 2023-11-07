from datetime import datetime

from decimal import Decimal

from django.utils import timezone

from app_products.models import Products

from django.db.models import Q

from celery import shared_task


@shared_task(ignore_result=True)
def check_discount_period():
        date_time_now = datetime.now()
        # TO DO CACHE
        all_products_with_discount = Products.objects.filter(
            Q(display_discount=True) | Q(display_promo=True)
        )
        for prod in all_products_with_discount:

            date_time_expirations_discont_prod = timezone.make_naive(prod.discount_period)

            date_time_expirations_discont_prod_PROMO = timezone.make_naive(
                prod.promo.discount_period_promo
            )

            # TO DO DRY
            price = Decimal(prod.price)
            if date_time_now > date_time_expirations_discont_prod and prod.display_discount:
                discount = Decimal(prod.discount) / 100
                price_with_discount_or_PROMO = prod.price_with_discount_or_PROMO
                price_without_discount = price_with_discount_or_PROMO + (price * discount)
                prod.price_with_discount_or_PROMO = price_without_discount
                prod.display_discount = False
                prod.save()
            
            if date_time_now > date_time_expirations_discont_prod_PROMO and prod.display_promo:
                discount = Decimal(prod.promo.discont_promo) / 100
                price_with_discount_or_PROMO = prod.price_with_discount_or_PROMO
                price_without_discount = price_with_discount_or_PROMO + (price * discount)
                prod.price_with_discount_or_PROMO = price_without_discount
                prod.display_promo = False
                prod.save()
