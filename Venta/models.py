from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Venta(models.Model):
    fecha= models.DateField(verbose_name="Fecha de Venta", help_text="MM/DD/AAAA")


