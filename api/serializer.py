from rest_framework import serializers
from products.models import *
from shop.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'created', 'in_stock', 'shop', 'category', 'price']


class RegisterShop(serializers.ModelSerializer):
    class Meta:
        model = ShopUnauthenticated
        fields = ['name', 'email', 'phone', 'address', 'country', 'zipcode', 'reviewed', 'otp']