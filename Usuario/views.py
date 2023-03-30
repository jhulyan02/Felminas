from django.shortcuts import render, redirect
from Usuario.models import Usuario
from Usuario.forms import UsuarioForm, UsuarioUpdateForm
# Create your views here.

def usuarios_crear(request):
    titulo="Usuario"
    if request.method== 'POST':
        form= UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Usuario')
    else:
        form= UsuarioForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"usuarios/crear.html", context )

def usuarios_listar(request):
    titulo="Usuario"
    usuarios= Usuario.objects.all()
    context={
        "titulo":titulo,
        "usuarios":usuarios
    }
    return render(request,"usuarios/listar.html", context)

def usuarios_modificar(request,pk):
    titulo="Usuario"
    usuario= Usuario.objects.get(id=pk)

    if request.method=='POST':
        form= UsuarioUpdateForm(instance=usuario)
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"usuarios/modificar.html", context)

def usuarios_eliminar(request,pk):
    usuario= Usuario.objects.filter(id=pk)
    usuario.update(
        estado="0"
    )
    return redirect('usuarios')
