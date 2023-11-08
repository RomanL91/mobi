from rest_framework import routers

from app_products.views import ProductViewSet, ProductImageViewSet


router = routers.SimpleRouter()

router.register(r'product', ProductViewSet)
router.register(r'improduct', ProductImageViewSet)
