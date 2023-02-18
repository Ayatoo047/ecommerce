from django.shortcuts import render, redirect
from users.models import *
from .forms import *

def addWorker(request):
    shop = Shop.objects.filter(owner__id=request.user.id).first()
    if request.method == 'POST':
        user_email = request.POST['email']
        user = User.objects.select_related('profile').filter(email=user_email).first()
        if request.user.id == shop.owner.id:
            Worker.objects.create(
                shop = shop,
                user = user
            )

    context = {'shop': shop}
    return render(request, 'shop/addworker.html', context)


def createProduct(request):
    shop = Shop.objects.filter(owner__id=request.user.id).first()
    worker = Worker.objects.filter(shop=shop).only('user')
    form = productCreationForm()
    if request.method == 'POST':
        if request.user in worker:
            print('validated')
            # form = productCreationForm(request.POST)
            # if form.is_valid:
            #     product = form.save(commit=False)
            #     product.shop = shop
            #     product.save()
            #     return redirect('index')

    context = {'shop':shop, 'form':form}
    return render(request, 'products/create.html', context)

def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = productCreationForm(instance=product)
    if request.method == 'POST':
        form = productCreationForm(request.POST, instance=product)
        if form.is_valid():
            product.save()
            return redirect('index')
    
    context = {'product':product, 'form':form}
    return render(request, 'products/create.html', context)

