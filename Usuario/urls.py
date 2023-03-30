from django.urls import path

from Usuario.views import usuarios_listar, usuarios_crear, usuarios_modificar, usuarios_eliminar

urlpatterns = [
    path('usuarios/', usuarios_listar, name="usuarios"),
    path('usuarios/crear/', usuarios_crear, name="usuarios-crear"),
    path('usuarios/modificar/<int:pk>/', usuarios_modificar, name="usuarios-modiicar"),
    path('usuarios/eliminar/<int:pk>/', usuarios_eliminar, name="usuarios-eliminar"),
]
