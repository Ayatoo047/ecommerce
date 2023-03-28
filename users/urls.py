from django.urls import path
from .views import loginUser, registerUser, verifyOtp

urlpatterns = [
    path('login/', loginUser, name='login'),
    path('register/', registerUser, name='register'),
    path('otpverification', verifyOtp, name='otpverification'),
    # path('product/<str:pk>/', singleProduct, name='product'),
]