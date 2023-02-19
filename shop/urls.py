from django.urls import path
from . import views

urlpatterns = [
    path('addworker/', views.addWorker, name='addworker'),
    path('updateproduct/<str:pk>/', views.updateProduct, name='updateproduct'),
    path('createproduct/', views.createProduct, name='create'),
    path('removeworker/', views.deleteWorker, name='removeworker'),
]
