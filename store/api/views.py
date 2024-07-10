from django.db.models import CharField, Q
from django.db.models.functions import Cast
from rest_framework import permissions, viewsets, views
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .. import models
from . import serializers


class CompaniesViewSet(viewsets.ModelViewSet):
    queryset = models.Companies.objects.all().order_by('-updated_at')
    serializer_class = serializers.CompaniesSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = models.Categories.objects.all().order_by('-updated_at')
    serializer_class = serializers.CategoriesSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = models.Products.objects.all().order_by('-updated_at')
    serializer_class = serializers.ProductsSerializer
    permission_classes = [permissions.IsAuthenticated]
