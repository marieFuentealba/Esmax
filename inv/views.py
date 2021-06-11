from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin

from .models import Categoria, SubCategoria, Producto, Bitacora
from .forms import CategoriaForm, SubCategoriaForm, ProductoForm, BitacoraForm

from bases.views import SinPrivilegios


class MixingFormInvalid:
        #duplicadp de datos
    def form_invalid(self, form):
        response = super().form_invalid(form)

        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response


class CategoriaView(SinPrivilegios, \
    generic.ListView):
    permission_required = "inv.view_categoria"
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"


class CategoriaNew(LoginRequiredMixin,MixingFormInvalid, generic.CreateView):
    model=Categoria
    template_name="inv/categoria_form.html"
    context_object_name = "obj"
    form_class= CategoriaForm
    success_url=reverse_lazy("inv:categoria_list")
    login_url = 'bases:login'

    #sobre escribir el metodo para tener acceso a la informacion y tomar el usuario logeado (id)

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class CategoriaEdit(LoginRequiredMixin, MixingFormInvalid, generic.UpdateView):
    model=Categoria
    template_name="inv/categoria_form.html"
    context_object_name = "obj"
    form_class= CategoriaForm
    success_url=reverse_lazy("inv:categoria_list")
    login_url = 'bases:login'

    #sobre escribir el metodo para tener acceso a la informacion y tomar el usuario logeado (id)

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


class CategoriaDelete(LoginRequiredMixin, generic.DeleteView):
    model=Categoria
    template_name='inv/categoria_delete.html'
    context_object_name = "obj"
    success_url=reverse_lazy("inv:categoria_list")


class SubCategoriaView( SinPrivilegios, \
    generic.ListView):
    permission_required= "inv.view_subcategoria"
    model = SubCategoria
    template_name = "inv/sub_categoria_list.html"
    context_object_name = "obj"
  
  
class SubCategoriaNew(LoginRequiredMixin,MixingFormInvalid, generic.CreateView):
    model=SubCategoria
    template_name="inv/sub_categoria_form.html"
    context_object_name = "obj"
    form_class= SubCategoriaForm
    success_url=reverse_lazy("inv:subcategoria_list")
    login_url = 'bases:login'

    #sobre escribir el metodo para tener acceso a la informacion y tomar el usuario logeado (id)

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class SubCategoriaEdit(LoginRequiredMixin, MixingFormInvalid, generic.UpdateView):
    model=SubCategoria
    template_name="inv/sub_categoria_form.html"
    context_object_name = "obj"
    form_class= SubCategoriaForm
    success_url=reverse_lazy("inv:subcategoria_list")
    login_url = 'bases:login'

    #sobre escribir el metodo para tener acceso a la informacion y tomar el usuario logeado (id)

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class SubCategoriaDelete(LoginRequiredMixin, generic.DeleteView):
    model=SubCategoria
    template_name='inv/subcategoria_delete.html'
    context_object_name = "obj"
    success_url=reverse_lazy("inv:subcategoria_list")

class ProductoView(LoginRequiredMixin, generic.ListView):
    model = Producto
    template_name = "inv/producto_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class ProductoNew(LoginRequiredMixin, generic.CreateView):
    model=Producto
    template_name="inv/producto_form.html"
    context_object_name = "obj"
    form_class= ProductoForm
    success_url=reverse_lazy("inv:producto_list")
    login_url = 'bases:login'


    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ProductoEdit(LoginRequiredMixin, generic.UpdateView):
    model=Producto
    template_name="inv/producto_form.html"
    context_object_name = "obj"
    form_class= ProductoForm
    success_url=reverse_lazy("inv:producto_list")
    login_url = 'bases:login'


    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class ProductoDelete(LoginRequiredMixin, generic.DeleteView):
    model=Producto
    template_name='inv/producto_delete.html'
    context_object_name = "obj"
    success_url=reverse_lazy("inv:producto_list")

def producto_inactivar(request, id):
    prod = Producto.objects.filter(pk=id).first()
    contexto={}
    template_name="inv:catalogos_del.html"

    if not prod:
        return redirect("inv:producto_list")

    if request.method =='GET':
        contexto={'obj':prod}
    
    if request.method =='POST':
        prod.estado=False
        prod.save()
        return redirect("inv:producto_list")
    
    return render(request,template_name,contexto)

class BitacoraView(LoginRequiredMixin, generic.ListView):
    model = Bitacora
    template_name = "inv/bitacora_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class BitacoraNew(LoginRequiredMixin, generic.CreateView):
    model=Bitacora
    template_name="inv/bitacora_form.html"
    context_object_name = "obj"
    form_class= BitacoraForm
    success_url=reverse_lazy("inv:bitacora_list")
    login_url = 'bases:login'

    #sobre escribir el metodo para tener acceso a la informacion y tomar el usuario logeado (id)

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class BitacoraEdit(LoginRequiredMixin, generic.UpdateView):
    model=Bitacora
    template_name="inv/bitacora_form.html"
    context_object_name = "obj"
    form_class= BitacoraForm
    success_url=reverse_lazy("inv:bitacora_list")
    login_url = 'bases:login'

    #sobre escribir el metodo para tener acceso a la informacion y tomar el usuario logeado (id)

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class BitacoraDelete(LoginRequiredMixin, generic.DeleteView):
    model=Bitacora
    template_name='inv/bitacora_delete.html'
    context_object_name = "obj"
    success_url=reverse_lazy("inv:bitacora_list")



