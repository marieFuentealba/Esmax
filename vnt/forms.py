from django import forms

from .models import Proveedor, VentasEnc

class ProveedorForm(forms.ModelForm):
    email = forms.EmailField(max_length=250)
    class Meta:
        model = Proveedor
        exclude = ['um','fm','uc_id','fc']
        widget = {'descripcion': forms.TextInput()}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
    
    def clean(self):
        try:
            sc = Proveedor.objects.get(
                descripcion=self.cleaned_data["descripcion"].upper()
            )

            if not self.instance.pk:
                print("Registro ya existe")
                raise forms.ValidationError("Registro Ya Existe")
            elif self.instance.pk!=sc.pk:
                print("Cambio no permitido")
                raise forms.ValidationError("Cambio No Permitido")
        except Proveedor.DoesNotExist:
            pass
        return self.cleaned_data



class VentasEncForm(forms.ModelForm):
    fecha_venta = forms.DateInput()
    fecha_factura = forms.DateInput()

    class Meta:
        model = VentasEnc
        fields= ['proveedor','fecha_venta','observacion','no_factura',
                'fecha_factura',
                'sub_total','descuento','total']
        widgets = {
            'fecha_factura': forms.DateInput(format=('%Y-%m-%d'), 
                                             attrs={'class':'myDateClass', 
                                            'placeholder':'Select a date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        ##self.fields['fecha_venta'].widget.attrs['readonly'] = True
        #self.fields['fecha_factura'].widget.attrs['readonly'] = True
        self.fields['sub_total'].widget.attrs['readonly'] = True
        self.fields['descuento'].widget.attrs['readonly'] = True
        self.fields['total'].widget.attrs['readonly'] = True