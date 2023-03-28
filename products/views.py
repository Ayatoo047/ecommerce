from django.shortcuts import render, redirect
import random
import json
from django.http import JsonResponse
from .models import * 


def numberofitem(request):
    cart, created = Cart.objects.get_or_create(owner=request.user.profile)
    cartitems = list(cart.cartitems.all())
    numbersof = len(cartitems)
    return int(numbersof)

def index(request):
    random_items = Product.objects.all().order_by('?')[:6]
    categories = Category.objects.all()

    promotion = Promotion.objects.all()
    if promotion is None:
        for produce in promotion:
            promo = produce.discount
    
    # cartsize = numberofitems(request)
    if promotion:
        context = {'random_items': random_items, 'categories': categories, 'promo':promo, 'promotion': promotion, 'cart': cart}
    else:
        context = {'random_items': random_items, 'categories': categories, 'cart': cart}
    return render(request, 'products/index.html', context)



def getCategory(request, pk):
    category = Category.objects.get(id=pk)
    products = Product.objects.filter(category__id=category.id)
    cart, created = Cart.objects.get_or_create(owner=request.user.profile)
    cartsize = numberofitem(request)


    context = {'category': category, 'products':products, 'cart': cart}
    return render(request, 'products/shop.html', context)

def singleProduct(request, pk):
    product = Product.objects.get(id=pk)
    products = Product.objects.all()
    cart, created = Cart.objects.get_or_create(owner=request.user.profile)
    cartsize = numberofitem(request)
    context = {'product': product, 'products':products, 'cart': cart}
    return render(request, 'products/shop-single.html', context)

def addtoCart(request):
    data = json.loads(request.body)
    product_id = data['id']
    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(owner=request.user.profile)
        cartitem, created = Cartitem.objects.get_or_create(cart=cart, product=product)
        cartitem.quantity += 1
        cartitem.save()
    return JsonResponse('It is clicked', safe=False)

def cart(request):
    cart = None
    cartitems = []

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(owner=request.user.profile)
        cartitems = cart.cartitems.all()
    
    # numberofitem = cartitems.count()
    cartsize = numberofitem(request)
    context = {'cart': cart, 'items': cartitems, }
    return render(request, 'products/cart.html', context)


def thankyou(request):
    return render(request, 'products/thankyou.html')


def deleteProduct(request):
    pass

def createCategory(request):
    pass

def createType(request):
    pass

def updateType(request):
    pass

def updateCategory(request):
    pass

