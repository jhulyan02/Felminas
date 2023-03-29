from django.db import models

# Create your models here.

primer_nombre= models.CharField(max_length=30, verbose_name="Primer Nombre")
segundo_nombre= models.CharField(max_length=30, verbose_name="Segundo Nombre")

primer_apellido= models.CharField(max_length=30, verbose_name="Primer Apellido")
segudno_apellido= models.CharField(max_length=30, verbose_name="Segundo Apellido")