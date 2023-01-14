from django.urls import path
from .views import loginUser

urlpatterns = [
    path('login/', loginUser, name='login'),
    # path('product/<str:pk>/', singleProduct, name='product'),
]