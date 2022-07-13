from email.mime import message
from pyexpat.errors import messages
from ssl import AlertDescription
import django
from django.shortcuts import render, redirect , get_object_or_404
from .models import Perrito, Producto 
from.forms import ProductoForm, CustomUserCreationForm, PerritoForm
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate, login
from .serializers import ProductoSerializer , PerritoSerializer
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

@api_view(['GET','POST'])
def producto_collection(request):
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','POST'])
def perrito_collection(request):
    if request.method == 'GET':
        perrito = Perrito.objects.all()
        serializer = PerritoSerializer(perrito, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PerritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def producto_element(request, pk):
    producto = get_object_or_404(Producto, id=pk)

    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        producto_new = JSONParser().parse(request) 
        serializer = ProductoSerializer(producto, data=producto_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def perrito_element(request, pk):
    perrito = get_object_or_404(Perrito, id=pk)

    if request.method == 'GET':
        serializer = PerritoSerializer(perrito)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        perrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        perrito_new = JSONParser().parse(request) 
        serializer = PerritoSerializer(perrito, data=perrito_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def home(request):
    return render(request,'app/home.html')

def index(request):
    return render(request,'app/index.html')

def pagina2(request):
    return render(request,'app/pagina2.html')

def pagina3(request):
    return render(request,'app/pagina3.html')

def pagina4(request):
    return render(request,'app/pagina4.html')

def agregar_producto(request):
    
    data = {
        'form': ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm (data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario
    
    return render(request, 'app/producto/agregar.html', data)

def listar_productos(request):
    productos= Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/producto/listar.html', data)

def modificar_producto(request, id):
    
    producto = get_object_or_404(Producto, id=id)
    
    data = {
        'form' : ProductoForm (instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm (data=request.POST,instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_productos")
        data["form"] = formulario
    
    return render(request, 'app/producto/modificar.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="listar_productos")
    
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="home")
        data["form"] = formulario
        
    return render (request,'registration/registro.html', data)



def agregar_perrito(request):
    
    data = {
        'form': PerritoForm()
    }
    
    if request.method == 'POST':
        formulario = PerritoForm (data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario
    
    return render(request, 'app/donar/agregar_perritos.html', data)

def listar_perritos(request):
    perrito = Perrito.objects.all()
    data = {
        'perritos': perrito
    }
    return render(request, 'app/donar/listar_perritos.html', data)

def modificar_perrito(request, id):
    
    perrito = get_object_or_404(Perrito, id=id)
    
    data = {
        'form' : PerritoForm (instance=perrito)
    }
    
    if request.method == 'POST':
        formulario = PerritoForm (data=request.POST,instance= perrito, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_perritos")
        data["form"] = formulario
    
    return render(request, 'app/donar/modificar_perritos.html', data)

def eliminar_perrito(request, id):
    perrito = get_object_or_404( Perrito, id=id)
    perrito.delete()
    return redirect(to="listar_perritos")