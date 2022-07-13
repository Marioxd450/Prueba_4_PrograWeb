from dataclasses import field
from numpy import source
from .models import Producto, Perrito
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    nombre_marca = serializers.CharField(read_only=True, source="marca.nombre")
    class Meta:
        model = Producto
        fields = '__all__'
        
        
class PerritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perrito
        fields = '__all__'