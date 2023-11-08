from rest_framework import routers

from app_products.views import ProductViewSet, ProductImageViewSet
from app_category.views import CategoryViewSet
from app_tags.views import TagViewSet


router = routers.SimpleRouter()

router.register(r'product', ProductViewSet)
router.register(r'improduct', ProductImageViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'tags', TagViewSet)
