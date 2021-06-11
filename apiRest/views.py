#CREAR ENDPOINT
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
#si busca un dato y no lo encuentra devuelve un 404
from django.shortcuts import get_object_or_404
#objeto  Q para fotrar query set codigo producto y cod barra condicional o
from django.db.models import Q


from .serializers import ProductoSerializer
from inv.models import Producto
#crear vista y hereda de apiview
class ProductoList(APIView):
    def get(self,request):
        prod = Producto.objects.all()
        data = ProductoSerializer(prod,many=True).data
        return Response(data)


class ProductoDetalle(APIView):
    def get(self,request, codigo):
        prod = get_object_or_404(Producto,Q(codigo=codigo)|Q(codigo_barra=codigo))
        data = ProductoSerializer(prod).data
        return Response(data)