from django.db import models

from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)
    uc = models.ForeignKey(User, on_delete=models.CASCADE)
    um = models.IntegerField(blank=True,null=True)

    class Meta:
        abstract=True

class ClaseModeloVersDos(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)
    # uc = models.ForeignKey(User, on_delete=models.CASCADE)
    # um = models.IntegerField(blank=True,null=True)
    usuario_crea = UserForeignKey(auto_user_add=True,related_name='+')
    usuario_modifica = UserForeignKey(auto_user=True,related_name='+')

    class Meta:
        abstract=True
