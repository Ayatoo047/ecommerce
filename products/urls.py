from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/<str:pk>/', getCategory, name='category'),
    path('product/<str:pk>/', singleProduct, name='product'),
    path('add_to_cart', addtoCart, name='addtocart'),
    path('cart/', cart, name='cart'),
    path('about/', about, name='about'),
    # path('thankyou', thankyou, name='thanks'),


    # path('', views.initiate_payment, name="initiate-payment"),
    # path('<str:ref>/', views.verify_payment, name="verify-payment"),
]