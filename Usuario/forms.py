from django import forms

from django.forms import ModelForm, widgets
from Usuario.models import Usuario

class UsuarioForm(ModelForm):

    class Meta:
        model = Usuario
        fields = "__all__"

        widgets={
            'fecha_nacimiento': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        }

class UsuarioUpdateForm(ModelForm):

    class Meta:
        model = Usuario
        fields = "__all__"
        exclude = ["documento","fecha_nacimiento"]

