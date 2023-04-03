from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet
from . serializer import *
from rest_framework.response import Response
from products.models import *

# Create your views here.

class ProductList(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def destroy(self, request, *args, **kwargs):
        product = Product.objects.get(id=kwargs['pk'])
        shop = Shop.objects.filter(id=request.user.worker.shop.id).first()
        if product.shop == shop: 
                product.delete()
        return super().destroy(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        # product = Product.objects.get(id=kwargs['pk'])
        
        shop = Shop.objects.filter(id=request.user.worker.shop.id)
        user_is_a_woker = shop.filter(workers__id=request.user.worker.id).exists()
        # shop = Shop.objects.filter(workers__id=request.user.id).exists()
        # workers = Worker.objects.filter(shop=shop).only('user')
        if user_is_a_woker:
            return super().update(request, *args, **kwargs)
    

class ShopViewSet(ModelViewSet):
     pass