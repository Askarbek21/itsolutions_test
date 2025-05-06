from django.urls import path, include
from rest_framework import routers

from .views import RecordAPIView

router = routers.SimpleRouter()
router.register(r'', RecordAPIView)

urlpatterns = [
    path('', include(router.urls)),
]
