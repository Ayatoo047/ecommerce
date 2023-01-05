from django.urls import path
from .views import index, singleProduct, getCategory

urlpatterns = [
    path('', index, name='index'),
    path('category/<str:pk>/', getCategory, name='category'),
    path('product/<str:pk>/', singleProduct, name='product'),
]