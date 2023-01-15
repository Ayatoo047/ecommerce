from django.db import models
import uuid
from users.models import Profile

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    in_stock = models.IntegerField(default=0)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    ptype = models.ForeignKey('ProductType', null=True, on_delete=models.SET_NULL)
    # store
    price = models.IntegerField()

    def __str__(self):
        return str(self.name)

class ProductType(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

class Category(models.Model):
    # product = models.ForeignKey('Product', null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

class Promotion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    maximum_time = models.TimeField()
    discount = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.product)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # review = models.TextChoices('Up': 'Up vote', 'Down': 'Down Vote')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    # reveiwer = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Cart(models.Model):
    owner = models.OneToOneField(Profile, blank=True, null=True, on_delete=models.CASCADE)
    # getproduct = models.ManyToManyField(Product, blank=True)
    total = models.IntegerField(default=0, null=True, blank=True )

    def __str__(self):
        return str(self.owner)

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
    
