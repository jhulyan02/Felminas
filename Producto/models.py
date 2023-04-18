from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Producto(models.Model):
    nombre= models.CharField(max_length=45, verbose_name="Nombre")
    descripcion= models.CharField(max_length=60, verbose_name="Descripcion")
    marca= models.CharField(max_length=30, verbose_name="Marca")


