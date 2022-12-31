from django.urls import path
from .views import index, getCategory

urlpatterns = [
    path('', index, name='index'),
    path('category/<str:pk>/', getCategory, name='category'),
]