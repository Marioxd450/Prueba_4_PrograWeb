from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Marca(models.Model):
        nombre = models.CharField(max_length=30)
        
        def __str__(self):
                return self.nombre

class Producto(models.Model):
        nombre = models.CharField(max_length=80)
        precio = models.IntegerField()
        marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
        imagen = models.ImageField(upload_to="productos",null=True)
        def __str__(self):
                return self.nombre
        
        
class Perrito(models.Model):
        nombre = models.CharField(max_length=80)
        raza = models.CharField(max_length=80)
        edad = models.IntegerField()
        imagen = models.ImageField(upload_to="perritos",null=True)
        def __str__(self):
                return self.nombre
        
