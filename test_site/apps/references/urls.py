from django.urls import path, include
from rest_framework import routers

from .views import (
StatusAPIView, TypeAPIView,
CategoryAPIView, SubCategoryAPIView
)

router = routers.SimpleRouter()
router.register(r'status', StatusAPIView)
router.register(r'type', TypeAPIView)
router.register(r'category', CategoryAPIView)
router.register(r'subcategory', SubCategoryAPIView)

urlpatterns = [
    path('', include(router.urls)),
]
