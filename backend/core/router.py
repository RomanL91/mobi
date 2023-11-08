from rest_framework import routers

from app_products.views import ProductViewSet, ProductImageViewSet
from app_category.views import CategoryViewSet


router = routers.SimpleRouter()

router.register(r'product', ProductViewSet)
router.register(r'improduct', ProductImageViewSet)
router.register(r'category', CategoryViewSet)
