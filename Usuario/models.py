from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Usuario(models.Model):
    primer_nombre= models.CharField(max_length=30, verbose_name="Primer Nombre")
    segundo_nombre= models.CharField(max_length=30, verbose_name="Segundo Nombre")

    primer_apellido= models.CharField(max_length=30, verbose_name="Primer Apellido")
    segudno_apellido= models.CharField(max_length=30, verbose_name="Segundo Apellido")

class Tipo_Documento(models.TextChoices):

    CEDULA='CC',_("Cedula")
    TARJETA='TI',_("Tarjeta de Idetidad")
    CEDULA_EXTRANJERIA='CE',_("Cédula de Extranjería")

tipo_documento= models.CharField(max_length=2, choices=Tipo_Documento.choices, verbose_name="Tipo de Documento")
Documento= models.CharField(max_length=20, verbose_name="Documento")

telefono_contacto=models.CharField(max_length=10, verbose_name="Telefono de contacto")
telefono_personal=models.CharField(max_length=10, verbose_name="telefono personal") 

class rol(models.TextField):
    EMPLEADO='E',_("Empleado")
    PROVEEDOR='P',_("Proveedor")
    CLIENTE='C',_("Cliente")
    
Rol=models.CharField(max_length=3, choices=rol.choices, verbose_name="Rol")

Correo=models.CharField(max_length=40, verbose_name="Correo")

class Estado(models.TextChoices):
    ACTIVO='1',_("Activo")
    INACTIVO='2',_("Inactivo")
    CONDICIONADO='3',_("Condicionado")
estado=models.CharField(max_length=15, verbose_name="Estado")

class Pago(models.Model):
    class Rol_Nivel(models.TextChoices):
        NIVELA='N1',_("nivel 1")
        NIVELB='N2',_("nivel 2")
        NIVELC='N3',_("nivel 3")
        NIVELD='N4',_("nivel 4")
        NIVELE='N5',_("nivel 5")

rol_nivel=models.CharField(max_length=5, verbose_name="nivel de roles")
fecha=models.DateField(verbose_name="Fecha", help_text="MM/DD/AAAA")

