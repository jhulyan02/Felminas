from django.urls import path

from usuario.views import usuario_listar, usuario_crear, usuario_modificar, usuario_eliminar

urlpatterns = [
    path('usuario/', usuario_listar, name="usuario"),
    path('usuario/crear/', usuario_crear, name="usuario-crear"),
    path('usuario/modificar/<int:pk>/', usuario_modificar, name="usuario-modificar"),
    path('usuario/eliminar/<int:pk>/', usuario_eliminar, name="usuario-eliminar"),
]
