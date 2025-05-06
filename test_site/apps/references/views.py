from rest_framework import viewsets

from .serializers import *


class StatusAPIView(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()


class TypeAPIView(viewsets.ModelViewSet):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()


class CategoryAPIView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SubCategoryAPIView(viewsets.ModelViewSet):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()

