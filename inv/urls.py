from django.urls import path

from .views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDelete,\
        SubCategoriaView, SubCategoriaNew, SubCategoriaEdit, SubCategoriaDelete,\
        ProductoView, ProductoNew, ProductoEdit,producto_inactivar, BitacoraView,\
        BitacoraNew, BitacoraEdit, BitacoraDelete, ProductoDelete

urlpatterns = [
    path('categorias/', CategoriaView.as_view(), name='categoria_list'),
    path('categorias/new', CategoriaNew.as_view(), name='categoria_new'),
    path('categorias/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
    path('categorias/delete/<int:pk>', CategoriaDelete.as_view(), name='categoria_delete'),

    path('subcategorias/', SubCategoriaView.as_view(), name='subcategoria_list'),
    path('subcategorias/new', SubCategoriaNew.as_view(), name='subcategoria_new'),
    path('subcategorias/edit/<int:pk>', SubCategoriaEdit.as_view(), name='subcategoria_edit'),
    path('subcategorias/delete/<int:pk>', SubCategoriaDelete.as_view(), name='subcategoria_delete'),

    path('producto/', ProductoView.as_view(), name='producto_list'),
    path('producto/new', ProductoNew.as_view(), name='producto_new'),
    path('producto/edit/<int:pk>', ProductoEdit.as_view(), name='producto_edit'),
    path('producto/delete/<int:pk>', ProductoDelete.as_view(), name='producto_delete'),
    path('producto/inactiva/<int:id>', producto_inactivar, name='producto_inactivar'),

    path('bitacora/', BitacoraView.as_view(), name='bitacora_list'),
    path('bitacora/new', BitacoraNew.as_view(), name='bitacora_new'),
    path('bitacora/edit/<int:pk>', BitacoraEdit.as_view(), name='bitacora_edit'),
    path('bitacora/delete/<int:pk>', BitacoraDelete.as_view(), name='bitacora_delete'),
    
]