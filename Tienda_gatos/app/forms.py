from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Producto
from .models import Perrito
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = '__all__'
        
        
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model=User
        fields= ['username',"first_name", "last_name", "email", "password1", "password2"]
        
        
class PerritoForm(forms.ModelForm):
    
    class Meta:
        model = Perrito
        fields = '__all__'
        
        
    