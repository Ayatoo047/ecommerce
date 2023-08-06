from django.shortcuts import render, redirect
from users.models import *
from . models import *
from .forms import *
from django.http import HttpResponse


def addWorker(request):
    if request.user.is_authenticated:
        shop_owner = request.user
        shop = Shop.objects.filter(owner=shop_owner).first()
        print(shop)
        if request.method == 'POST':
            user_email = request.POST['email']
            worker = User.objects.select_related('profile').filter(email=user_email).first()
            if request.user.shop.id == shop.owner.id:
                Worker.objects.create(
                    shop = shop,
                    user = worker
                )
    else:
        return redirect('login')
    context = {'shop': shop}
    return render(request, 'shop/addworker.html', context)

def deleteWorker(request):
    if request.user.is_authenticated:
        shop = Shop.objects.filter(owner__id=request.user.shop.id).first()
        if request.method == 'POST':
            user_email = request.POST['email']
            worker = Worker.objects.prefetch_related('user').filter(user__email=user_email).first()
            if request.user.shop.id == shop.owner.id:
                worker.delete()
            else:
                HttpResponse('unauthorized')
        context = {'shop': shop}
        return render(request, 'shop/addworker.html', context)
    else:
        return HttpResponse('unauthorized')


def createProduct(request):
    if request.user.is_authenticated:

        shop = Shop.objects.filter(id=request.user.worker.shop.id).first()
        user_is_a_woker = Shop.objects.filter(workers__id=request.user.worker.id).exists()
        # shop = Shop.objects.filter(workers__id=request.user.id).exists()
        # workers = Worker.objects.filter(shop=shop).only('user')
        form = productCreationForm()
        if request.method == 'POST':
            if user_is_a_woker: 
                form = productCreationForm(request.POST)
                if form.is_valid:
                    product = form.save(commit=False)
                    product.shop = shop
                    product.save()
                    return redirect('index')
            else:
                return HttpResponse('unauthorized')
        context = {'shop':shop, 'form':form}
        return render(request, 'shop/create.html', context)
    else:
        return HttpResponse('unauthorized')


def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = productCreationForm(instance=product)
    shop = Shop.objects.filter(id=request.user.worker.shop.id).first()
    user_is_a_woker = Shop.objects.filter(workers__id=request.user.worker.id).exists()
    # shop = Shop.objects.filter(workers__id=request.user.id).exists()
    # workers = Worker.objects.filter(shop=shop).only('user')
    form = productCreationForm()
    if request.method == 'POST':
        if user_is_a_woker: 
            form = productCreationForm(request.POST, instance=product)
            if form.is_valid():
                product.save()
                return redirect('index')
            else:
                HttpResponse("bad data")
        else:
            HttpResponse('unauthorized')
    
    context = {'product':product, 'form':form}
    return render(request, 'shop/create.html', context)

def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)

    shop = Shop.objects.filter(id=request.user.worker.shop.id).first()
    # user_is_a_woker = Shop.objects.filter(workers__id=request.user.worker.id).exists()

    if request.method == 'POST':
        if product.shop == shop: 
                product.delete()
                return redirect('index')
        else:
            HttpResponse('you are not authorized')
    context = {'product':product}
    return render(request, 'shop/create.html', context)

def authShop(request):
    unauth_shops = ShopUnauthenticated.objects.filter(authenticated=False)

    context = {'unauth_shop': unauth_shops}
    return render(request, 'shop/unauthshop.html', context)

def single_unauth_shop(request, pk):
    shop = ShopUnauthenticated.objects.get(id=pk)

    if request.method == 'POST':
        newshop = Shop.objects.create(
            name = shop.name,
            owner = shop.owner,
            email = shop.email,
            address = shop.address,
            phone = shop.phone,
            zipcode = shop.zipcode,
            country = shop.country
        )

        shop.reviewed = True
        shop.authenticated = True

        Worker.objects.create(
            user = shop.owner,
            shop = newshop
            )
    return render(request, 'shop/single_unath.html', {'shop':shop})
        