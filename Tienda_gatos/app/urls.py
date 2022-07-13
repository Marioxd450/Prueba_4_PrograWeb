from django.urls import path , include
from .views import home, index, pagina2, pagina3, pagina4, agregar_producto, listar_productos , modificar_producto, eliminar_producto , perrito_element , registro, producto_collection, producto_element , perrito_collection , agregar_perrito ,listar_perritos, modificar_perrito, eliminar_perrito
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
    path('apiii/',  perrito_collection , name='perrito_collection'),
    path('apiii/<int:pk>/', perrito_element ,name='perrito_element'),
    path('agregar-perritos/', agregar_perrito, name="agregar_perrito"),
    path('listar-perritos/',listar_perritos, name="listar_perritos"),
    path('modificar-perritos/<id>/', modificar_perrito, name="modificar_perrito"),
    path('eliminar-perritos/<id>/',eliminar_perrito, name="eliminar_perrito"),
]

