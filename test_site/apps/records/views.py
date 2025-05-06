from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *


class RecordAPIView(viewsets.ModelViewSet):
    serializer_class = RecordSerializer
    queryset = Record.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['created_at', 'status', 'type', 'category', 'subcategory']


