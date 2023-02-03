from django.db import models
from django.contrib.auth.models import User
# from products.models import Cart
class Otp(models.Model):
    otp = models.CharField(max_length=6, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=11)
    # dob = 
    address = models.CharField(max_length=500)
    country = models.CharField(max_length=300, null=True)
    zipcode = models.CharField(max_length=10, null=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    # cart = models.OneToOneField(Cart, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
    

