from django.forms import ModelForm
from .models import *

class productCreationForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price']

