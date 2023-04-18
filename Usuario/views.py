from django.shortcuts import render, redirect
from usuario.models import Usuario
from usuario.forms import UsuarioForm, UsuarioUpdateForm
# Create your views here.

def usuario_crear(request):
    titulo="Usuario"
    if request.method== 'POST':
        form= UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario')
    else:
        form= UsuarioForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"usuario/crear.html", context )

def usuario_listar(request):
    titulo="Usuario"
    usuarios= Usuario.objects.all()
    context={
        "titulo":titulo,
        "usuarios":usuarios
    }
    return render(request,"usuario/listar.html", context)

def usuario_modificar(request,pk):
    titulo="Usuario"
    usuario= Usuario.objects.get(id=pk)

    if request.method=='POST':
        form= UsuarioUpdateForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario')
    else:
        form= UsuarioUpdateForm(instance=usuario)
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"usuario/modificar.html", context)

def usuario_eliminar(request,pk):
    usuario= Usuario.objects.filter(id=pk)
    usuario.update(
        estado="0"
    )
    return redirect('usuario')
