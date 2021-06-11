from django import forms

from .models import Categoria, SubCategoria, Producto, Bitacora


class CategoriaForm( forms.ModelForm):
    class Meta:
        model=Categoria
        fields = ['descripcion', 'estado']
        labels = {'descripcion':'Descripcion de la Categoria xx',
                    'estado':'Estado'}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
    def clean(self):
        try:
            sc = Categoria.objects.get(
                descripcion=self.cleaned_data["descripcion"].upper()
            )

            if not self.instance.pk:
                print("Registro ya existe")
                raise forms.ValidationError("Registro Ya Existe")
            elif self.instance.pk!=sc.pk:
                print("Cambio no permitido")
                raise forms.ValidationError("Cambio No Permitido")
        except Categoria.DoesNotExist:
            pass
        return self.cleaned_data

class SubCategoriaForm( forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True)
        .order_by('descripcion')
    )
    class Meta:
        model=SubCategoria
        fields = ['categoria','descripcion', 'estado']
        labels = {'descripcion':'Sub Categoria',
                    'estado':'Estado'}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        
        self.fields['categoria'].empty_label = "Seleccione Categoria"
    
    def clean(self):
        try:
            sc = SubCategoria.objects.get(
                descripcion=self.cleaned_data["descripcion"].upper()
            )

            if not self.instance.pk:
                print("Registro ya existe")
                raise forms.ValidationError("Registro Ya Existe")
            elif self.instance.pk!=sc.pk:
                print("Cambio no permitido")
                raise forms.ValidationError("Cambio No Permitido")
        except SubCategoria.DoesNotExist:
            pass
        return self.cleaned_data

class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields=['codigo','codigo_barra','descripcion','estado',\
            'precio','existencia','fecha_carga','cantidad', \
            'comentario', 'subCategoria']
        exclude=['um','fm','uc_id','fc',]
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
    
        self.fields['fecha_carga'].widget.attrs['readonly'] = True
       # self.fields['existencia'].widget.attrs['readonly'] = True
   

class BitacoraForm(forms.ModelForm):
    class Meta:
        model=Bitacora
        fields=['codigo','numero_documento','numero_viaje','fecha_recepcion',\
            'hora_recepcion','subCategoria','ubicacion','inicial', \
            'final', 'litros_recibidos','diferencia', 'tk','temperatura',\
            'api', 'descripcion']
        exclude=['um','fm','uc_id','fc',]
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
    
    

