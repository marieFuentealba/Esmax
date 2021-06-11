from django.urls import path, include
#importar vistas de view.py
from .views import ProductoList, ProductoDetalle


urlpatterns = [
    path('v1/productos/',ProductoList.as_view(),name='producto_list'),
    #va a recibir una variable tipo cadena
    path('v1/productos/<str:codigo>',ProductoDetalle.as_view(),name='producto_detalle'),
]