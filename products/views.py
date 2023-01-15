from django.shortcuts import render
import random
import json
from django.http import JsonResponse
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

def singleProduct(request, pk):
    product = Product.objects.get(id=pk)
    # product = Product.objects.get(id=pk)
    # cart = request.user.profile.cart
    products = Product.objects.all()
    # cart = products.
    
    # if request.method == 'POST':
    #     # owner = request.user.profile,
    #     # product = cart.getproduct.add(product.id)
    #     # print(owner, product)
    #     Cart.objects.create(
    #         owner = request.user.profile,
    #         getproduct = product.cart.set([product])
    #         # total = goods.price
    #     )
    context = {'product': product, 'products':products}
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
    
    context = {'cart': cart, 'items': cartitems}
    return render(request, 'products/cart.html', context)

def checkout(request):

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(owner=request.user.profile)
        cartitems = cart.cartitems.all()
    
    context = {'cart': cart, 'items': cartitems}
    return render(request, 'products/checkout.html', context)

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


