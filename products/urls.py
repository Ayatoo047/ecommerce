from django.urls import path
from .views import index, singleProduct, getCategory, addtoCart, cart

urlpatterns = [
    path('', index, name='index'),
    path('category/<str:pk>/', getCategory, name='category'),
    path('product/<str:pk>/', singleProduct, name='product'),
    path('add_to_cart', addtoCart, name='addtocart'),
    path('cart', cart, name='cart'),
]