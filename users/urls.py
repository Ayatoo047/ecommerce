from django.urls import path
from .views import loginUser, registerUser, verifyOtp, adminpanel, logoutuser

urlpatterns = [
    path('login/', loginUser, name='login'),
    path('logout/', logoutuser, name='logout'),
    path('register/', registerUser, name='register'),
    path('otpverification', verifyOtp, name='otpverification'),
    path('adminpanel', adminpanel, name='adminpanel'),
]