from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ShopUnauthenticated(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='shopowner')
    # workers = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='workers')
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=11)
    profile_image = models.ImageField(null=True, blank=True)
    # verification = models.ImageField(null=True)
    address = models.CharField(max_length=500)
    country = models.CharField(max_length=300, null=True)
    zipcode = models.CharField(max_length=10, null=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    reviewed = models.BooleanField(default=False)
    authenticated = models.BooleanField(default=False)
    date_requested = models.DateTimeField(auto_now_add=True)
    date_reviewed = models.DateTimeField(auto_now=True)
    # otp = models.models.ForeignKey(Otp, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return str(self.name)
    

class ShopUnauthVerifyImages(models.Model):
    images = models.ImageField()
    forshop = models.ForeignKey(ShopUnauthenticated, on_delete=models.CASCADE, related_name='shopdocs')
    

