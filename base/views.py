from django.shotcuts import redirect, render

def principal(request):
    titulo="Inicio"
    context={
        "titulo":titulo
    }
    return render(request, "index.html",context)