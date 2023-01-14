from django.db import models
from django.contrib.auth.models import User
# from products.models import Cart

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=11)
    # dob = 
    address = models.CharField(max_length=500)
    # cart = models.OneToOneField(Cart, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
    

