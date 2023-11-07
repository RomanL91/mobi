from rest_framework import routers

from app_products.views import ProductViewSet


router = routers.SimpleRouter()

router.register(r'product', ProductViewSet)
