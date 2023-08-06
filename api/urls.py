from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('allproducts', views.ProductList)
# router.register('registershop', views.RegisterShop,)
router.urls

print(router.urls)
urlpatterns = path('', include(router.urls)),
