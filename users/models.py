from django.db import models
from django.contrib.auth.models import User
import datetime
# from products.models import Cart


class Otp(models.Model):
    profile = models.ForeignKey('Profile', null=True, blank=True, on_delete=models.CASCADE, related_name='otp')
    otp = models.CharField(max_length=6, null=True, blank=True)
    created = models.DateTimeField(auto_now=True, null=True)
    # duration = models.DurationField(default=datetime.timedelta(days =-1, seconds = 68400))

    def __str__(self):
        return str(self.otp)


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=11)
    # profile_image image = models.ImageField(null=True, blank=True)
    # dob = 
    address = models.CharField(max_length=500)
    country = models.CharField(max_length=300, null=True)
    zipcode = models.CharField(max_length=10, null=True)
    # otp = models.CharField(max_length=6, null=True, blank=True)
    # otp = models.ForeignKey(Otp, on_delete=models.CASCADE, null=True, blank=True)
    # cart = models.OneToOneField(Cart, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Shop(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='shop')
    # workers = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='workers')
    # first_name = models.CharField(max_length=200)
    # last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=11)
    profile_image = models.ImageField(null=True, blank=True)
    # dob = 
    address = models.CharField(max_length=500)
    country = models.CharField(max_length=300, null=True)
    zipcode = models.CharField(max_length=10, null=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    # otp = models.models.ForeignKey(Otp, on_delete=models.CASCADE, null=True, blank=True)
    # cart = models.OneToOneField(Cart, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Worker(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, null=True, blank=True, on_delete=models.CASCADE, related_name='workers')


    def __str__(self):
        shop_workers = str(self.user)
        return shop_workers
    