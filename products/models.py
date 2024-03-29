from django.db import models
import uuid
from users.models import Profile, Shop

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    in_stock = models.IntegerField(default=0)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    ptype = models.ForeignKey('ProductType', null=True, on_delete=models.SET_NULL, blank=True)
    # store
    price = models.IntegerField()

    def __str__(self):
        return str(self.name)

class ProductType(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

class Category(models.Model):
    # product = models.ForeignKey('Product', null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

class Promotion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    maximum_time = models.TimeField()
    discount = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.product)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # review = models.TextChoices('Up': 'Up vote', 'Down': 'Down Vote')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    # reveiwer = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Cart(models.Model):
    owner = models.OneToOneField(Profile, blank=True, null=True, on_delete=models.CASCADE)
    # getproduct = models.ManyToManyField(Product, blank=True)
    total = models.IntegerField(default=0, null=True, blank=True )

    def __str__(self):
        return str(self.owner)

    @property
    def grandtotal(self):
        cartitems = self.cartitems.all()
        grandtotal = sum([item.price for item in cartitems])
        return grandtotal

    @property
    def numberofitem(self):
        itemsall = self.cartitems.all()
        numberofitem = len(itemsall)
        return numberofitem

class Cartitem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitems')
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.product)
        

    @property
    def price(self):
        final_price = self.quantity * self.product.price
        return final_price

    @property
    def numberofitem(self):
        itemsall = self.cartitems.all()
        numberofitem = len(itemsall)
        return numberofitem
    

class Order(models.Model):
    owner = models.OneToOneField(Profile, blank=True, null=True, on_delete=models.CASCADE) 
    is_verified = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    # @property
    # def number_of_items(self, request):
    #     cart = Cart.objects.get(owner=request.user.profile)
    #     cartitems = cart.cartitems.all()

    #     numberof = cartitems.count()
    #     return numberof

class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    orderitems = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)