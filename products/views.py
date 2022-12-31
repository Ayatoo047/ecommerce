from django.shortcuts import render
import random
from .models import * 

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    random_items = products.order_by('?')[:6]

    promotion = Promotion.objects.all()
    for produce in promotion:
        promo = produce.discount * 100

    context = {'products': products, 'random_items': random_items, 'categories': categories, 'promo':promo, 'promotion': promotion}
    return render(request, 'products/index.html', context)

def getCategory(request, pk):
    # product = Product.objects.get(id=pk)
    category = Category.objects.get(id=pk)
    # product = Product.objects.all()
    products = Product.objects.all()
    # Product.category_set.all()
    context = {'category': category, 'products':products}
    return render(request, 'products/shop.html', context)

def createProduct(request):
    pass

def createCategory(request):
    pass

def createType(request):
    pass

def updateType(request):
    pass

def updateCategory(request):
    pass

def updateProduct(request):
    pass

def deleteProduct(request):
    pass

def a_product(request, pk):
    product = Product.objects.get(id=pk)
    
    context = {'product': product}
    pass


