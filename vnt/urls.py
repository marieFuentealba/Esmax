from django.urls import path, include

from .views import ProveedorView,ProveedorNew,ProveedorEdit, \
    proveedorInactivar, VentasView, ventas

from .reportes import reporte_ventas, imprimir_venta

urlpatterns = [
    path('proveedores/', ProveedorView.as_view(), name='proveedores_list'),
    path('proveedores/new', ProveedorNew.as_view(), name='proveedores_new'),
    path('proveedores/edit/<int:pk>', ProveedorEdit.as_view(), name='proveedores_edit'),
    path('proveedores/inactiva/<int:id>', proveedorInactivar, name='proveedor_inactivar'),

    path('ventas/', VentasView.as_view(), name='ventas_list'),
    path('ventas/new', ventas, name='ventas_new'),
    path('ventas/edit/<int:venta_id>',ventas, name="ventas_edit"),

    path('ventas/listado', reporte_ventas, name='ventas_print_all'),
    path('ventas/<int:venta_id>/imprimir', imprimir_venta,name="ventas_print_one"),


 
]