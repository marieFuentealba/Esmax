from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
import datetime
from django.http import HttpResponse

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
import json
from django.db.models import Sum

from .models import Proveedor, VentasEnc, VentasDet
from vnt.forms import ProveedorForm, VentasEncForm
from inv.models import Producto 

class MixingFormInvalid:
        #duplicadp de datos
    def form_invalid(self, form):
        response = super().form_invalid(form)

        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

class ProveedorView(LoginRequiredMixin, generic.ListView):
    model = Proveedor
    template_name = "vnt/proveedor_list.html"
    context_object_name = "obj"

    login_url = 'bases:login'


class ProveedorNew(LoginRequiredMixin,MixingFormInvalid, generic.CreateView):
    model = Proveedor
    template_name = "vnt/proveedor_form.html"
    context_object_name = "obj"
    form_class = ProveedorForm
    success_url=reverse_lazy("vnt:proveedores_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)



class ProveedorEdit(LoginRequiredMixin, MixingFormInvalid, generic.UpdateView):
    model=Proveedor
    template_name="vnt/proveedor_form.html"
    context_object_name = "obj"
    form_class= ProveedorForm
    success_url=reverse_lazy("vnt:proveedores_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

def proveedorInactivar(request,id):
    template_name="vnt/inactivar_proveedor.html"
    contexto= {}
    proveedor = Proveedor.objects.filter(pk=id).first()

    if not proveedor:
        return HttpResponse('Proveedor no Existe' + str(id))
    
    if request.method=='GET':
        contexto = {'obj':proveedor}
    
    if request.method=='POST':
        proveedor.estado = False
        proveedor.save()
        contexto = {'obj':'OK'}
        return HttpResponse('Proveedor Inactivado')


    return render(request,template_name,contexto)

class VentasView(LoginRequiredMixin, generic.ListView):
    model = VentasEnc
    template_name = "vnt/ventas_list.html"
    context_object_name = "obj"
    form_class= ProveedorForm
    success_url=reverse_lazy("vnt:ventas_list")
    login_url = 'bases:login'


@login_required(login_url="/login/")
@permission_required("vnt.view_ventasenc'",login_url='bases:sin_privilegios')
def ventas(request, venta_id=None):
    template_name = 'vnt/ventas.html'
    producto = Producto.objects.filter(estado = True)
    form_ventas = {}
    contexto = {}

    if request.method=='GET':
        form_ventas= VentasEncForm()
        encabezado = VentasEnc.objects.filter(pk=venta_id).first()

        if encabezado:
            detalle = VentasDet.objects.filter(venta= encabezado)
            fecha_venta = datetime.date.isoformat(encabezado.fecha_venta)
            fecha_factura = datetime.date.isoformat(encabezado.fecha_factura)
            e = {
                'fecha_venta': fecha_venta,
                'proveedor': encabezado.proveedor,
                'observacion': encabezado.observacion,
                'no_factura' : encabezado.no_factura,
                'fecha_factura' : encabezado.fecha_factura,
                'sub_total' : encabezado.sub_total,
                'descuento': encabezado.descuento,
                'total' : encabezado.total
            }

            form_ventas = VentasEncForm(e)
        else:
            detalle =  None
        contexto={'productos': producto, 'encabezado': encabezado, 'detalle': detalle, 'form_encabezado': form_ventas}


        #capturar todo el formulario

    if request.method== 'POST':
        #obtener con request.POST.get
        fecha_venta = request.POST.get("fecha_venta")
        observacion = request.POST.get("observacion")
        no_factura = request.POST.get("no_factura")
        fecha_factura = request.POST.get("fecha_factura")
        proveedor = request.POST.get("proveedor")
        #inicializar variables
        sub_total = 0
        descuento = 0
        total = 0

        #consultar por encabezado si existe

        if not venta_id:
            #guardar proveedor
            proveedor=Proveedor.objects.get(pk=proveedor)
            #inicializar

            encabezado = VentasEnc(
                fecha_venta=fecha_venta,
                observacion=observacion,
                no_factura=no_factura,
                fecha_factura=fecha_factura,
                proveedor=proveedor,
                uc = request.user
            )

            if encabezado:
                encabezado.save()
                venta_id = encabezado.id
        else:
            encabezado = VentasEnc.objects.filter(pk=venta_id).first()
            if encabezado:
                #actualizar 
                encabezado.fecha_venta = fecha_venta
                encabezado.observacion = observacion
                encabezado.no_factura = no_factura
                encabezado.fecha_factura = fecha_factura
                #usuario modifica
                encabezado.um = request.user.id
                encabezado.save()
        #si venta id no tiene nada
        if not venta_id:
            return redirect("vnt:ventas_list")

        #capturar datos del producto que se han enviado para el detalle

        producto = request.POST.get("id_id_producto")
        cantidad = request.POST.get("id_cantidad_detalle")
        precio = request.POST.get("id_precio_detalle")
        sub_total_detalle = request.POST.get("id_sub_total_detalle")
        descuento_detalle  = request.POST.get("id_descuento_detalle")
        total_detalle  = request.POST.get("id_total_detalle")

        prod = Producto.objects.get(pk=producto)

        detalle = VentasDet(
            venta = encabezado,
            producto = prod,
            cantidad = cantidad,
            precio_prv = precio,
            descuento = descuento_detalle,
            costo = 0,
            uc = request.user
        )

        if detalle:
            detalle.save()

            sub_total=VentasDet.objects.filter(venta=venta_id).aggregate(Sum('sub_total'))
            descuento = VentasDet.objects.filter(venta = venta_id ).aggregate(Sum('descuento'))

            encabezado.sub_total = sub_total["sub_total__sum"]
            encabezado.descuento = descuento["descuento__sum"]
            encabezado.save()
        
        return redirect("vnt:ventas_edit", venta_id = venta_id)

    



        

    return render(request, template_name, contexto)


    
