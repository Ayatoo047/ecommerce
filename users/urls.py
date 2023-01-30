from django.urls import path
from .views import loginUser, registerUser

urlpatterns = [
    path('login/', loginUser, name='login'),
    path('register/', registerUser, name='register'),
    # path('product/<str:pk>/', singleProduct, name='product'),
]