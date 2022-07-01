from django.urls import path , include
from .views import home, index, pagina2, pagina3, pagina4, agregar_producto, listar_productos , modificar_producto, eliminar_producto , registro, producto_collection, producto_element
from rest_framework.decorators import api_view




urlpatterns = [
    path('',home,name="home"),
    path('index/',index, name="index"),
    path('contacto/',pagina2, name="contacto"),
    path('tienda/',pagina3, name="tienda"),
    path('api/',pagina4, name="api"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/',listar_productos, name="listar_productos"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/',eliminar_producto, name="eliminar_producto"),
    path('registro/', registro, name="registro"),
    path('apii/',  producto_collection , name='producto_collection'),
    path('apii/<int:pk>/', producto_element ,name='producto_element'),
]

