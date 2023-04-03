from rest_framework import serializers
from products.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'created', 'in_stock', 'shop', 'category', 'price']


class RegisterShop(serializers.ModelSerializer):
    pass