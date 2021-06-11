from django.db import models

from bases.models import ClaseModelo

class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de la categoria',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()
    
    class Meta:
        verbose_name_plural= "Categorias"


class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de la sub categoria'     
    )
    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion, self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()

    class Meta:
        verbose_name_plural= "Sub Categorias"
        unique_together = ('categoria', 'descripcion')

class Producto(ClaseModelo):
    subCategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    codigo = models.CharField(
        max_length=20,
        unique=True
    )
    codigo_barra = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField(default=0)
    existencia = models.IntegerField(default=12)
    fecha_carga = models.DateField(null=True, blank=True)
    cantidad = models.IntegerField(default=0)
    comentario = models.CharField(max_length=200)


    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Producto, self).save()
    
    class Meta:
        verbose_name_plural= "Productos"
        unique_together = ('codigo', 'codigo_barra')

class Bitacora(ClaseModelo):
    codigo = models.CharField(
        max_length=20,
        unique=True
    )
    subCategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    numero_documento = models.IntegerField(default=0)
    numero_viaje = models.IntegerField(default=0)
    fecha_recepcion = models.DateField(null=True, blank=True)
    hora_recepcion = models.DateField(null=True, blank=True)
    ubicacion = models.CharField(max_length=200)
    inicial = models.IntegerField(default=0)
    final = models.IntegerField(default=0)
    litros_recibidos = models.IntegerField(default=0)
    diferencia = models.IntegerField(default=0)
    tk = models.IntegerField(default=0)
    temperatura = models.IntegerField(default=0)
    api = models.FloatField(default=0)
    descripcion = models.CharField(max_length=200)
    

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Bitacora, self).save()

    class Meta:
        verbose_name_plural= "Bitacoras"
        

    
