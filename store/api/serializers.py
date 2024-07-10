from rest_framework import serializers

from .. import models


class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Companies
        fields = [
            'business_name',
            'registration_name',
            'ruc',
            'website',
            'id', 'key',
            'active',
        ]


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categories
        fields = [
            'name',
            'id', 'active',
        ]


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Products
        fields = [
            'company',
            'business_name',
            'registration_name',
            'gtin', 'gtin_type',
            'categories',
            'id','active',
            'key',
        ]
