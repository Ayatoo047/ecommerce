from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/<str:pk>/', Category, name='category'),
    path('product/<str:pk>/', singleProduct, name='product'),
    path('updateproduct/<str:pk>/', updateProduct, name='updateproduct'),
    path('add_to_cart', addtoCart, name='addtocart'),
    path('cart', cart, name='cart'),
    path('checkout', checkout, name='checkout'),
    path('thankyou', thankyou, name='thanks'),
    path('createproduct/', createProduct, name='create'),
]