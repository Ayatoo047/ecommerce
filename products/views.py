from django.shortcuts import render, redirect
import random
import json
from django.http import JsonResponse
from .models import * 
from .forms import *

def numberofitem(request):
    cart = Cart.objects.get(owner=request.user.profile)
    cartitems = list(cart.cartitems.all())
    numbersof = len(cartitems)
    return int(numbersof)

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    random_items = products.order_by('?')[:6]

    promotion = Promotion.objects.all()
    for produce in promotion:
        promo = produce.discount * 100

    # cartsize = numberofitems(request)
 
    context = {'products': products, 'random_items': random_items, 'categories': categories, 'promo':promo, 'promotion': promotion, 'cart': cart}
    return render(request, 'products/index.html', context)



def getCategory(request, pk):
    category = Category.objects.get(id=pk)
    products = Product.objects.all()
    cart = Cart.objects.get(owner=request.user.profile)
    cartsize = numberofitem(request)
    context = {'category': category, 'products':products, 'cart': cart}
    return render(request, 'products/shop.html', context)

def singleProduct(request, pk):
    product = Product.objects.get(id=pk)
    products = Product.objects.all()
    cart = Cart.objects.get(owner=request.user.profile)
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

def checkout(request):
    profile = request.user.profile
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(owner=request.user.profile)
        cartitems = cart.cartitems.all()
    
    context = {'cart': cart, 'items': cartitems, 'profile': profile}
    return render(request, 'products/checkout.html', context)

def thankyou(request):
    return render(request, 'products/thankyou.html')

def createProduct(request):
    shop = Shop.objects.filter(owner__id=request.user.id).first()
    form = productCreationForm()
    if request.method == 'POST':
        form = productCreationForm(request.POST)
        if form.is_valid:
            product = form.save(commit=False)
            product.shop = shop
            product.save()
            return redirect('index')

    context = {'shop':shop, 'form':form}
    return render(request, 'products/create.html', context)

def createCategory(request):
    pass

def createType(request):
    pass

def updateType(request):
    pass

def updateCategory(request):
    pass

def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = productCreationForm(instance=product)
    if request.method == 'POST':
        form = productCreationForm(request.POST, instance=product)
        if form.is_valid:
            product.save()
    
    context = {'product':product, 'form':form}
    return render(request, 'products/create.html', context)

def deleteProduct(request):
    pass


